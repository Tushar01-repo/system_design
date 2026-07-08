# ------------------------------------- IDEMPOTENCY DESIGN -----------------------------------------------------

#  ----------------------------------- THIS IS PHASE 2 IMPLEMENTATION -----------------------------------

# The next thing I would implement

# Now that entities are almost complete, the next important flow is:

# Create Show
#       ↓
# Generate ShowSeats from Screen Seats
#       ↓
# Lock Seats
#       ↓
# Create Booking
#       ↓
# Make Payment
#       ↓
# Confirm Booking
#       ↓
# Cancel Booking

# This is where interviewers usually start asking questions on:

# seat locking
# preventing double booking
# timers (5 min hold)
# concurrency
# race conditions
# idempotent payments


from enum import Enum
from datetime import datetime, timedelta
import threading


# ENUMS definition
class SeatBookingStatus(Enum):
    AVAILABLE = "AVAILABLE"
    BOOKED = "BOOKED"
    LOCKED = "LOCKED"


class BookingStatus(Enum):
    CREATED = "CREATED"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"


class PaymentStatus(Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class SeatType(Enum):
    REGULAR = "REGULAR"
    PREMIUM = "PREMIUM"
    RECLINER = "RECLINER"


# System Design Level Classes
class IdempotencyRecord:
    def __init__(self, key, payment):
        self.key = key
        self.payment = payment


# Entity classes
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"user_id : {self.user_id}, name : {self.name}, email : {self.email}"


class Movie:
    def __init__(self, movie_id, movie_name, movie_duration, movie_language, movie_genre):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.movie_duration = movie_duration
        self.movie_language = movie_language
        self.movie_genre = movie_genre

    def __repr__(self):
        return (
            f"Movie("
            f"id={self.movie_id}, "
            f"name={self.movie_name}, "
            f"duration={self.movie_duration}, "
            f"language={self.movie_language}, "
            f"genre={self.movie_genre}"
            f")"
        )


class Theatre:
    def __init__(self, theatre_id, theatre_name, theatre_location):
        self.theatre_id = theatre_id
        self.theatre_name = theatre_name
        self.theatre_location = theatre_location
        self.screens = []

    def add_screens(self, screen):
        self.screens.append(screen)

    def __repr__(self):
        return (
            f"Theatre("
            f"theatre_id={self.theatre_id}, "
            f"theatre_name={self.theatre_name}, "
            f"theatre_location={self.theatre_location}, "
            f"screen={self.screens}"
            f")"
        )


class Seat:
    def __init__(self, seat_id, row, number, seat_type, price):
        self.seat_id = seat_id
        self.row = row
        self.number = number
        self.seat_type = seat_type
        self.price = price

    def __repr__(self):
        return (
            f"Seat("
            f"id={self.seat_id}, "
            f"row={self.row}, "
            f"number={self.number}, "
            f"type={self.seat_type.value}, "
            f"price={self.price}"
            f")"
        )


class Screen:
    def __init__(self, screen_id, name):
        self.screen_id = screen_id
        # here name is screen name like audi 1, audi 2 etc
        self.name = name
        self.seats = []

    def add_seats(self, seat):
        self.seats.append(seat)

    def __repr__(self):
        return (
            f"Screen Details("
            f"screen_id={self.screen_id}, "
            f"name={self.name}, "
            f"seats={self.seats}"
            f")"
        )


class Show:
    def __init__(self, show_id, movie, screen, start_time, end_time):
        self.show_id = show_id
        self.movie = movie
        self.screen = screen
        self.start_time = start_time
        self.end_time = end_time
        self.show_seats = []

    def add_show_seat(self, show_seat):
        self.show_seats.append(show_seat)

    def __repr__(self):
        return (
            f"Show Details("
            f"show_id={self.show_id}, "
            f"movie={self.movie}, "
            f"screen={self.screen}, "
            f"start_time={self.start_time}, "
            f"end_time={self.end_time}, "
            f"show_seat={self.show_seats}"
            f")"
        )


class Booking:
    def __init__(self, book_id, user, show, booked_seats, total_amount, status):
        self.book_id = book_id
        self.user = user
        self.show = show
        self.booked_seats = booked_seats
        self.total_amount = total_amount
        self.status = status

    def booking_confirm(self):
        self.status = BookingStatus.CONFIRMED

    def booking_cancel(self):
        self.status = BookingStatus.CANCELLED

    def booking_created(self):
        self.status = BookingStatus.CREATED


# preventing RACE conditions
class ShowSeat:
    def __init__(self, show_seat_id, seat, status=SeatBookingStatus.AVAILABLE):
        self.show_seat_id = show_seat_id
        self.seat = seat
        self.status = status
        self.locked_by = None
        self.locked_at = None

        self.lock = threading.Lock()

    def __repr__(self):
        return (
            f"Showseat("
            f"id={self.show_seat_id}, "
            f"seat={self.seat.seat_id}, "
            f"status={self.status.value}"
            f")"
        )

    def seat_available(self):
        return self.status == SeatBookingStatus.AVAILABLE

    def seat_locked(self, user):
        self.status = SeatBookingStatus.LOCKED
        self.locked_by = user
        self.locked_at = datetime.now()

    def seat_booked(self):
        self.status = SeatBookingStatus.BOOKED

    def seat_release(self):
        self.status = SeatBookingStatus.AVAILABLE
        self.locked_by = None
        self.locked_at = None


class Payment:
    def __init__(self, payment_id, booking, amount, status):
        self.payment_id = payment_id
        self.booking = booking
        self.amount = amount
        self.status = status


# business logic class must be separated because interviewer expects this
class BookingService:

    # this is the state that should store the data for business logic
    def __init__(self):
        self.movies = []
        self.users = []
        self.theatres = []
        self.bookings = []
        self.payment = []
        self.shows = []
        self.seats = []

        # ---------------------------
        # Idempotency
        # ---------------------------
        self.idempotency_store = {}

        # key -> threading.Lock()
        self.payment_locks = {}

        # protects payment_locks map
        self.payment_locks_lock = threading.Lock()

    def get_payment_lock(self, key):
        with self.payment_locks_lock:
            if key not in self.payment_locks:
                self.payment_locks[key] = threading.Lock()
            return self.payment_locks[key]

    def add_user(self, user):
        self.users.append(user)

    def add_movies(self, movie):
        self.movies.extend(movie)

    def add_theatre(self, theatre):
        self.theatres.extend(theatre)

    def add_show(self, show):
        self.shows.append(show)

        for seat in show.screen.seats:
            show_seat = ShowSeat(
                show_seat_id=f"{show.show_id} - {seat.seat_id}",
                seat=seat
            )
            show.add_show_seat(show_seat)

    def create_booking(self, user, show, show_seat_id):

        if user not in self.users:
            raise Exception("Invalid User")

        if show not in self.shows:
            raise Exception("Invalid Show")

        selected_show_seat = [
            show_seat
            for show_seat in show.show_seats
            if show_seat.seat.seat_id in show_seat_id
        ]

        # Lock seats (atomic: all-or-nothing, see lock_seat)
        self.lock_seat(user, selected_show_seat)

        # Calculate amount
        total_amount = sum(
            show_seat.seat.price
            for show_seat in selected_show_seat
        )

        booking = Booking(
            book_id=f"BOOK-{len(self.bookings) + 1}",
            user=user,
            show=show,
            booked_seats=selected_show_seat,
            total_amount=total_amount,
            status=BookingStatus.CREATED
        )

        self.bookings.append(booking)

        return booking

    def lock_seat(self, user, show_seats):
        """
        Locks every requested seat, or none at all.
        If any seat in the batch is unavailable, every seat that was
        already locked earlier in this same call is released again,
        so a failed booking never leaves "orphaned" locked seats behind.
        """
        locked_so_far = []

        try:
            for show_seat in show_seats:
                with show_seat.lock:
                    if not show_seat.seat_available():
                        raise Exception(
                            f"{show_seat.seat.seat_id} unavailable"
                        )
                    show_seat.seat_locked(user)
                    locked_so_far.append(show_seat)

        except Exception:
            for show_seat in locked_so_far:
                with show_seat.lock:
                    show_seat.seat_release()
            raise

    def confirm_booking(self, booking, payment):
        if payment.status != PaymentStatus.SUCCESS:
            raise Exception("payment failed....")

        booking.booking_confirm()

        for show_seat in booking.booked_seats:
            show_seat.seat_booked()

        return booking

    def make_payment(self, payment_id, booking, payment_method, idempotency_key):

        if booking.status != BookingStatus.CREATED:
            raise Exception("Booking not valid")

        payment_lock = self.get_payment_lock(idempotency_key)

        with payment_lock:

            # If we've already processed this exact request before,
            # short-circuit and hand back the original result instead
            # of hitting the payment gateway again.
            if idempotency_key in self.idempotency_store:
                print(
                    f"[IDEMPOTENT] RETURNING EXISTING PAYMENT "
                    f"FOR KEY = {idempotency_key}"
                )
                return self.idempotency_store[idempotency_key].payment

            print("calling payment gateway......")

            payment = Payment(
                payment_id=payment_id,
                booking=booking,
                amount=booking.total_amount,
                status=PaymentStatus.PENDING
            )

            ###################################
            # imagine this as razorpay, stripe
            ###################################
            payment_success = True
            if payment_success:
                payment.status = PaymentStatus.SUCCESS
            else:
                payment.status = PaymentStatus.FAILED

            self.payment.append(payment)

            ######################################
            # store result so retries with the same
            # idempotency_key are served from here
            ######################################
            self.idempotency_store[idempotency_key] = IdempotencyRecord(
                idempotency_key, payment
            )

            return payment

    def cancel_booking(self, booking):
        booking.booking_cancel()

        for show_seat in booking.booked_seats:
            show_seat.seat_release()

    def generate_ticket(self, booking):
        if booking.status != BookingStatus.CONFIRMED:
            raise Exception("Booking not confirmed")

        print("=" * 40)
        print("MOVIE TICKET")
        print("=" * 40)

        print("Movie :", booking.show.movie.movie_name)
        print("User :", booking.user.name)

        print("Seats :", end=" ")
        for seat in booking.booked_seats:
            print(f"{seat.seat.row}{seat.seat.number}", end=" ")
        print()

        print("Amount :", booking.total_amount)
        print("=" * 40)

    # LOCK_DURATION = timedelta(minutes=5)
    LOCK_DURATION = timedelta(seconds=10)

    def release_expired_locks(self, show):
        for show_seat in show.show_seats:
            if (
                show_seat.status == SeatBookingStatus.LOCKED
                and datetime.now() - show_seat.locked_at > self.LOCK_DURATION
            ):
                show_seat.seat_release()


if __name__ == "__main__":

    booking_service = BookingService()

    # ---------------- Users ----------------
    user1 = User("id-101", "Tushar", "tushar@gmail.com")
    user2 = User("id-102", "Rahul", "rahul@gmail.com")

    booking_service.add_user(user1)
    booking_service.add_user(user2)

    # ---------------- Movies ----------------
    movie = Movie("mid-101", "Batman", "2.5 hr", "English", "Thriller")
    booking_service.add_movies([movie])

    # ---------------- Theatre ----------------
    theatre = Theatre("th-101", "PVR", "Delhi")
    screen = Screen("scr-101", "Audi-1")

    screen.add_seats(Seat("se-101", "A", "1", SeatType.REGULAR, 200))
    screen.add_seats(Seat("se-102", "A", "2", SeatType.REGULAR, 200))
    screen.add_seats(Seat("se-103", "A", "3", SeatType.REGULAR, 200))

    theatre.add_screens(screen)
    booking_service.add_theatre([theatre])

    # ---------------- Show ----------------
    show = Show("show-101", movie, screen, "1 PM", "4 PM")
    booking_service.add_show(show)

    # =========================================================
    # DEMO 1: two users racing for the SAME seat (lock_seat test)
    # =========================================================
    print("\n--- DEMO 1: concurrent booking of the same seat ---")

    def try_booking(user, results):
        try:
            booking = booking_service.create_booking(
                user=user,
                show=show,
                show_seat_id=["se-101"]
            )
            results[user.user_id] = booking
            print(f"{user.name} locked/booked se-101 successfully.")
        except Exception as e:
            print(f"{user.name} failed -> {e}")

    results = {}
    t1 = threading.Thread(target=try_booking, args=(user1, results))
    t2 = threading.Thread(target=try_booking, args=(user2, results))
    t1.start()

    
    t2.start()
    t1.join()
    t2.join()

    print("Seat status after race:", show.show_seats[0])

    # Whoever won the race gets a real Booking object we can pay for.
    winning_booking = next(iter(results.values()))

    # =========================================================
    # DEMO 2: same payment request fired twice concurrently
    # (idempotency_key test) -> gateway should only be called once
    # =========================================================
    print("\n--- DEMO 2: duplicate/concurrent payment requests ---")

    def retry_payment():
        payment = booking_service.make_payment(
            payment_id="PAY-101",
            booking=winning_booking,
            payment_method="UPI",
            idempotency_key="payment-101"
        )
        print(
            threading.current_thread().name,
            "->",
            payment.payment_id,
            payment.status
        )

    pt1 = threading.Thread(target=retry_payment, name="Thread-1")
    pt2 = threading.Thread(target=retry_payment, name="Thread-2")
    pt1.start()
    pt2.start()
    pt1.join()
    pt2.join()

    final_payment = booking_service.idempotency_store["payment-101"].payment
    booking_service.confirm_booking(winning_booking, final_payment)

    print("\nBooking status:", winning_booking.status)
    print("Final Seat Status:")
    for seat in show.show_seats:
        print(seat.show_seat_id, seat.status)

    booking_service.generate_ticket(winning_booking)