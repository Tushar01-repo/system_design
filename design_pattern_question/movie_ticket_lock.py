# ------------------------------------- LOCK DESIGN -----------------------------------------------------

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


# Entity classes
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __repr__(self):
        return (
            f"user_id : {self.user_id}, name : {self.name}, email : {self.email}"
        )


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

import threading

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




# business logic class must be seperated becuase interviewer expect this 
class BookingService:

    # this is the state that should store the data for business logic 
    def __init__(self):
        self.movies = []
        self.users = []
        self.theatres= []
        self.bookings = []
        self.payment = []
        self.shows = []
        self.seats = []


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

    # def create_booking(self, user, show, show_seat_id):
    #     if user not in self.users:
    #         raise Exception("Invalid User, please create an account first")
        
    #     if show not in self.shows:
    #         raise Exception("Invalid show selected, please try again...")
        
    #     # if show_seat_id not in self.seats:
    #     #     raise Exception("Selected seat is not valid, please try again...")

    #     selected_show_seat = []

    #     for show_seat in show.show_seats:
    #         if show_seat.seat.seat_id in show_seat_id:

    #             if not show_seat.seat_available():
    #                 raise Exception(
    #                     f"{show_seat.seat.seat_id} is unavailable"
    #                 )
                
    #             selected_show_seat.append(show_seat)

    #     self.lock_seat(selected_show_seat)

    #     total_amount = 0

    #     for show_seat in show.show_seats:
    #         if show_seat.seat.seat_id in selected_show_seat:
    #             if not show_seat.seat_available():
    #                 raise Exception("seat unavaialble")
                
    #             selected_show_seat.append(show_seat)
    #             total_amount += show_seat.seat.price


    def create_booking(self, user, show, show_seat_id):

        if user not in self.users:
            raise Exception("Invalid User")

        if show not in self.shows:
            raise Exception("Invalid Show")

        selected_show_seat = []

        for show_seat in show.show_seats:

            if show_seat.seat.seat_id in show_seat_id:

                if not show_seat.seat_available():
                    raise Exception(
                        f"{show_seat.seat.seat_id} unavailable"
                    )

                selected_show_seat.append(show_seat)

        # Lock seats
        self.lock_seat(user, selected_show_seat)

        # Calculate amount
        total_amount = sum(
            show_seat.seat.price
            for show_seat in selected_show_seat
        )

        booking = Booking(
            book_id=f"BOOK-{len(self.bookings)+1}",
            user=user,
            show=show,
            booked_seats=selected_show_seat,
            total_amount=total_amount,
            status=BookingStatus.CREATED
        )

        self.bookings.append(booking)

        return booking



    # def lock_seat(self, user, show_seat_id):

    #     with self.lock:
    #         for show_seat in show_seat_id:
    #             if not show_seat.seat_available():
    #                 raise Exception(
    #                     f"{show_seat.seat.seat_id} unavailable"
    #                 )
                    
    #             show_seat.seat_locked(user)


    def lock_seat(self, user, show_seats):
        for show_seat in show_seats:
            with show_seat.lock:

                if not show_seat.seat_available():
                    raise Exception(
                        f"{show_seat.seat.seat_id} unavailable"
                    )
                
                show_seat.seat_locked(user)


    def confirm_booking(self, booking, payment):
        if payment.status != PaymentStatus.SUCCESS:
            raise Exception("payment failed....")
        
        booking.booking_confirm()

        for show_seat in booking.booked_seats:
            show_seat.seat_booked()

        return booking
    

    def make_payment(self, payment_id, booking, payment_method):
        
        if booking.status != BookingStatus.CREATED:
            raise Exception("Booking not valid")
        
        payment = Payment(
            payment_id=payment_id,
            booking=booking,
            amount=booking.total_amount,
            status=PaymentStatus.PENDING
        )

        payment_success = True

        if payment_success:
            payment.status = PaymentStatus.SUCCESS

        else:
            payment.status = PaymentStatus.FAILED

        self.payment.append(payment)

        return payment

    def cancel_booking(self, booking):
        booking.booking_cancel()

        for show_seat in booking.booked_seats:
            show_seat.seat_release()


    def generate_ticket(self, booking):
        if booking.status != BookingStatus.CONFIRMED:
            raise Exception("Booking not confirmed")
        
        print("="*40)
        print("MOVIE TICKET")
        print("="*40)

        print("Movie :", booking.show.movie.movie_name)
        print("User :", booking.user.name)

        print("Seats :", end=" ")

        for seat in booking.booked_seats:
            print(
                f"{seat.seat.row}{seat.seat.number}",
                end=" "
            )

        print()
        print("Amount :", booking.total_amount)
        print("="*40)


    # LOCK_DURATION = timedelta(minutes=5)
    LOCK_DURATION = timedelta(seconds=10)
    
    def release_expired_locks(self, show):
        for show_seat in show.show_seats:
            if (show_seat.status==SeatBookingStatus.LOCKED and datetime.now() - show_seat.locked_at > self.LOCK_DURATION):
                show_seat.seat_release()




# if __name__ == "__main__":

#     user = User('id-101', "tushar", "tushar@gmail.com")
#     booking_service = BookingService()
#     booking_service.add_user(user)

#     print(booking_service.users)

#     movie_1 = Movie("mid-101", "batman", "2.5 hr", "english", "thriller")
#     movie_2 = Movie("mid-102", "cocktail", "2 hr", "hindi", "romcom")

#     booking_service.add_movies([movie_1, movie_2])
#     print(booking_service.movies)

#     theatre_1 = Theatre("th-101", "PVR", "delhi")
#     theatre_2 = Theatre("th-102", "INOX", "bengaluru")

#     screen_1 = Screen("scr-101", "audi-1")
#     screen_2 = Screen("scr-102", "audi-2")

#     # # this is a wrong method, as it is creating a list of list
#     # screen_1.add_seats(["A1", "A2", "A3"])
#     # screen_2.add_seats(["B1", "B2", "B3"])


#     # seats is a class so it should be added as an object
#     seat_11 = Seat("se-101", "A", "1", SeatType.REGULAR, 200)
#     seat_12 = Seat("se-102", "A", "2", SeatType.REGULAR, 200)
#     seat_13 = Seat("se-103", "A", "3", SeatType.REGULAR, 200)
#     seat_21 = Seat("se-104", "B", "1", SeatType.REGULAR, 200)
#     seat_22 = Seat("se-105", "B", "2", SeatType.REGULAR, 200)
#     seat_23 = Seat("se-106", "B", "3", SeatType.REGULAR, 200)

#     screen_1.add_seats(seat_11)
#     screen_1.add_seats(seat_12)
#     screen_1.add_seats(seat_13)
#     screen_2.add_seats(seat_21)
#     screen_2.add_seats(seat_22)
#     screen_2.add_seats(seat_23)

#     theatre_1.add_screens(screen_1)
#     theatre_2.add_screens(screen_2)

#     booking_service.add_theatre([theatre_1, theatre_2])
#     print(booking_service.theatres)

#     show_1 = Show("show-101", movie_1, screen_1, "1 pm", "4 pm")
#     show_2 = Show("show-102", movie_2, screen_2, "6 pm", "9 pm")

#     adding_show_1 = booking_service.add_show(
#         show_1
#     )

#     create_booking_1 = booking_service.create_booking(
#         user=user,
#         show=show_1,
#         show_seat_id=["se-101", "se-103"]

#     )

#     print(show_1.show_seats)

#     Payment_status = booking_service.make_payment("payId-101",create_booking_1,"UPI")

#     booking_service.confirm_booking(
#         create_booking_1,
#         Payment_status
#     )

#     print(create_booking_1.status)
#     print(Payment_status.status)


# seat locking main function
# if __name__ == "__main__":

#     user = User('id-101', "tushar", "tushar@gmail.com")
#     booking_service = BookingService()
#     booking_service.add_user(user)

#     print(booking_service.users)

#     movie_1 = Movie("mid-101", "batman", "2.5 hr", "english", "thriller")
#     movie_2 = Movie("mid-102", "cocktail", "2 hr", "hindi", "romcom")

#     booking_service.add_movies([movie_1, movie_2])
#     print(booking_service.movies)

#     theatre_1 = Theatre("th-101", "PVR", "delhi")
#     theatre_2 = Theatre("th-102", "INOX", "bengaluru")

#     screen_1 = Screen("scr-101", "audi-1")
#     screen_2 = Screen("scr-102", "audi-2")

#     # # this is a wrong method, as it is creating a list of list
#     # screen_1.add_seats(["A1", "A2", "A3"])
#     # screen_2.add_seats(["B1", "B2", "B3"])


#     # seats is a class so it should be added as an object
#     seat_11 = Seat("se-101", "A", "1", SeatType.REGULAR, 200)
#     seat_12 = Seat("se-102", "A", "2", SeatType.REGULAR, 200)
#     seat_13 = Seat("se-103", "A", "3", SeatType.REGULAR, 200)
#     seat_21 = Seat("se-104", "B", "1", SeatType.REGULAR, 200)
#     seat_22 = Seat("se-105", "B", "2", SeatType.REGULAR, 200)
#     seat_23 = Seat("se-106", "B", "3", SeatType.REGULAR, 200)

#     screen_1.add_seats(seat_11)
#     screen_1.add_seats(seat_12)
#     screen_1.add_seats(seat_13)
#     screen_2.add_seats(seat_21)
#     screen_2.add_seats(seat_22)
#     screen_2.add_seats(seat_23)

#     theatre_1.add_screens(screen_1)
#     theatre_2.add_screens(screen_2)

#     booking_service.add_theatre([theatre_1, theatre_2])
#     print(booking_service.theatres)

#     show_1 = Show("show-101", movie_1, screen_1, "1 pm", "4 pm")
#     show_2 = Show("show-102", movie_2, screen_2, "6 pm", "9 pm")

#     adding_show_1 = booking_service.add_show(
#         show_1
#     )

#     create_booking_1 = booking_service.create_booking(
#         user=user,
#         show=show_1,
#         show_seat_id=["se-101", "se-103"]

#     )

#     import time
    
#     print("\n Seat booked before the release....")
#     print(show_1.show_seats)
#     time.sleep(11)
    
#     print("\n Seat release after the locking timeout....")

#     booking_service.release_expired_locks(show_1)
#     print(show_1.show_seats)

#     Payment_status = booking_service.make_payment("payId-101",create_booking_1,"UPI")

#     booking_service.confirm_booking(
#         create_booking_1,
#         Payment_status
#     )

#     print(create_booking_1.status)
#     print(Payment_status.status)


import threading

if __name__ == "__main__":

    booking_service = BookingService()

    # ---------------- Users ----------------

    user1 = User("id-101", "Tushar", "tushar@gmail.com")
    user2 = User("id-102", "Rahul", "rahul@gmail.com")

    booking_service.add_user(user1)
    booking_service.add_user(user2)

    # ---------------- Movies ----------------

    movie = Movie(
        "mid-101",
        "Batman",
        "2.5 hr",
        "English",
        "Thriller"
    )

    booking_service.add_movies([movie])

    # ---------------- Theatre ----------------

    theatre = Theatre(
        "th-101",
        "PVR",
        "Delhi"
    )

    screen = Screen(
        "scr-101",
        "Audi-1"
    )

    # ---------------- Seats ----------------

    screen.add_seats(
        Seat("se-101", "A", "1", SeatType.REGULAR, 200)
    )

    screen.add_seats(
        Seat("se-102", "A", "2", SeatType.REGULAR, 200)
    )

    screen.add_seats(
        Seat("se-103", "A", "3", SeatType.REGULAR, 200)
    )

    theatre.add_screens(screen)
    booking_service.add_theatre([theatre])

    # ---------------- Show ----------------

    show = Show(
        "show-101",
        movie,
        screen,
        "1 PM",
        "4 PM"
    )

    booking_service.add_show(show)

    # ---------------- Thread Function ----------------

    def try_booking(user):

        try:

            booking = booking_service.create_booking(
                user=user,
                show=show,
                show_seat_id=["se-101"]
            )

            payment = booking_service.make_payment(
                payment_id=f"PAY-{user.user_id}",
                booking=booking,
                payment_method="UPI"
            )

            booking_service.confirm_booking(
                booking,
                payment
            )

            print(f"{user.name} booked successfully.")

        except Exception as e:

            print(f"{user.name} failed -> {e}")

    # ---------------- Threads ----------------

    thread1 = threading.Thread(
        target=try_booking,
        args=(user1,)
    )

    thread2 = threading.Thread(
        target=try_booking,
        args=(user2,)
    )

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("\nFinal Seat Status:")

    for seat in show.show_seats:
        print(
            seat.show_seat_id,
            seat.status
        )