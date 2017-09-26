"""
Uses Book and Person classes to implement a simple library.
"""

class Book:
    # parameters:
        title: string
        author: string
        publication_date: date
        call_number: string
        subject: string
        borrower: Person
        return_date: date
        hold_for: Person

    # methods:
        check_out(Book, borrower, return_date)
            # If the book is not alreayd borrowed...
            # Is this a valid borrower
            if (borrower is a Person who is_Borrower):
                Book.borrower = borrower
                # Make sure the return_date is in the future, but not too far into the future.
                # Default is not more than 180 days.
                if (return date is > 180 days):
                    Print a message ... cannot borrow but for 180 days.
                    Use the 180th day as the return date
                Book.return_date = return_date
            else (explain this person cannot borrow books)

        check_in(Book)
        hold(book, hold_for_person)
        renew(book, new_return_date)

        # def renew(which_book, due_date):
        #     duration = 60 days
        #     is there someone in the hold queue?
        #       no:
                    # Is today within 30 days of the due date?
                    # yes:
                    #     new_due_date = today + duration
                    #     change due_date of which_book to new_due_date
                    # no:
                        # "Come back on [date]."
        #       yes, someone is waiting for this book:
        #           "Sorry, this book cannot be renewed."

	#prompts to enter all the new book information
    def create(title, author, subject, pub_date, call_number)
    	title = input("Enter title")
    	author = input("Enter one or more authors")
    	subject = input("Enter one or more subjects")
    	pub_date = input(date)
    	call_number = input("Enter call number")

        give_away(Book)

class Person
