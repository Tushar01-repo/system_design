from datetime import datetime, timedelta

class Book:
    def __init__(self,book_id, book_title, book_author, book_isbn, book_year):
        self.book_id = book_id
        self.book_title = book_title
        self.book_author = book_author
        self.book_isbn = book_isbn
        self.book_year = book_year


class BookItem:
    def __init__(self, book_copy_id, book):
        self.book_copy_id = book_copy_id
        #.book_title = book_title
        # here we are using book class bcz if book we pass then explicity we don't need to pass title
        # and if let say tomorrow we want to fetch author name, isbn from book item then we can easily fetched it from 
        # book class bcz it carries everything instead of just book name 
        self.book = book
        self.book_available = True

    def is_available(self):
        return self.book_available
    
    def mark_issued(self):
        self.book_available = False
    
    def mark_available(self):
        self.book_available = True


class Library:
    def __init__(self):
        self.books = []
        self.book_items = []
        self.members = []
        self.issue_records = []
    
    # here we are calling add_books method which will call the BOOK class which will add books 
    def add_books(self, book):
        self.books.append(book)

    # here we are calling members class which will append members details
    def register_member(self, member):
        self.members.append(member)

    # here we are calling book_item class, which will append book details copy 
    def add_book_item(self,book_items):
        self.book_items.extend(book_items)

    # this is the main method to call issue_book function which will implement end to end functionality for issuing a book
    def issue_book(self, member, book):
        available_copy = None

        if member not in self.members:
            raise Exception("Member not registered")
        
        if not member.can_borrow():
            raise Exception("member reached the limit to borrow the books i.e. 5")
        
        if book not in self.books:
            raise Exception("Book is not available")
        
        for item in self.book_items:
            if item.book == book and item.is_available():
                available_copy = item
                break

        if available_copy is None:
            raise Exception(f"No copies for this book is available")
        
        available_copy.mark_issued()

        issue_date = datetime.now()
        due_date = issue_date + timedelta(days=14)

        book_issue_record = IssueRecord(
            member,
            available_copy,
            issue_date,
            due_date

        )

        print(book_issue_record)

        self.issue_records.append(book_issue_record)
        member.member_borrowed_book.append(book_issue_record)

        return book_issue_record


    # here we implement the function to return the book
    def return_book(self, issue_record):
        if issue_record not in self.issue_records:
            raise Exception("Invalid issue records")
        
        issue_record.issued_book_return_date = datetime.now()
        issue_record.issued_book_item.mark_available()

        member = issue_record.issued_book_member

        if issue_record in member.member_borrowed_book:
            member.member_borrowed_book.remove(issue_record)



class Member:

    MAX_BOOKS = 5

    def __init__(self, member_id, member_name, member_email):
        self.member_id = member_id
        self.member_name = member_name
        self.member_email = member_email
        # if we are defining the list here, please remember don't pass it as a param in init
        # else it will be unused param 
        self.member_borrowed_book = []

    def can_borrow(self):
        print(f"yes, the member can still borrow the book {len(self.member_borrowed_book)}")
        return len(self.member_borrowed_book)< self.MAX_BOOKS


class IssueRecord:
    def __init__(self, issued_book_member, issued_book_item, issued_book_date, issued_book_due_date):
        self.issued_book_member = issued_book_member
        self.issued_book_item = issued_book_item
        self.issued_book_date = issued_book_date
        self.issued_book_due_date = issued_book_due_date
        self.issued_book_return_date = None

    def __repr__(self):
        return (
            f"IssueRecord("
            f"member={self.issued_book_member.member_name}, "
            f"book={self.issued_book_item.book.book_title}, "
            f"copy_id={self.issued_book_item.book_copy_id}, "
            f"issue_date={self.issued_book_date}, "
            f"due_date={self.issued_book_due_date}, "
            f"return_date={self.issued_book_return_date}"
            f")"
        )


if __name__ == "__main__":

    library = Library()
    # add a book
    harry_potter_1 = Book(
        "hp_b_1",
        "Harry Potter Part 1",
        "JK Rowling",
        "ISBN1234",
        2001,
    )

    # adding copies of same book
    harry_potter_2 = BookItem(
        "hp_b_2",
        harry_potter_1
    )

    harry_potter_3 = BookItem(
        "hp_b_3",
        harry_potter_1
    )

    
    # registration of member in the library 
    alice_registration = Member(
        1,
        "Alice",
        "alice@gmail.com",
    )

    # here we are passing complete object of python, not a single string 
    library.register_member(alice_registration)
    library.add_books(harry_potter_1)

    # library.book_items.append(harry_potter_2)
    # library.book_items.append(harry_potter_3)
    # for interview level please use below method
    
    # library.book_items.extend(
    #     [harry_potter_2, harry_potter_3]
    # )

    library.add_book_item([harry_potter_2, harry_potter_3])

    # issuing a book
    alice = library.issue_book(
        alice_registration,
        harry_potter_1
    )

    alice = library.issue_book(
        alice_registration, 
        harry_potter_1
    )

    alice = library.issue_book(
        alice_registration, 
        harry_potter_1
    )

    # here it may exhaust as we don't have too many books
    alice = library.issue_book(
        alice_registration, 
        harry_potter_1
    )

    print(f"{alice.issued_book_member.member_name} borrowed "
          f"{alice.issued_book_item.book.book_title}"
          )

        