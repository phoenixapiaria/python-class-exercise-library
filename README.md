# python-class-exercise-library
Exercise about objects & classes, using a library as an example

# User stories

## Add a book to the library

Bob, a librarian, wants to create a book & add it to the library.


## Renewal

Alice, a borrower, wants to renew a book so that she can continue to read it. She asks Bob, a librarian, to renew the book in the system.
* A book may be renewed indefinitely if no one is in the hold queue.
* The default renewal period is 60 days, but Bob can choose a different due date.
* A book may be renewed within 30 days before its due (if no one is in the hold queue).
* The renewal period starts from the day of the renewal request.

## Hold a book

Lily, a borrower, wants to borrow a book, but it's already checked out, so now she wants to put it on hold. She asks Bob, a librarian, to put the book on hold for her.
* When a book is on hold, it can't be renewed.
* If there are already people in line to hold a book, Lily will be next in line.
