import csv
"Commer seperated values to write and load fron or in to it"
class Book:
    """
    Represents a book with a title, author, genre, ISBN, status (available or borrowed)
    and borrower information
    """

    def __init__(self, title, author, genre, ISBN):
        """
        Initializes a new Book object with the given attributes

        Args:
        title (str): Title of the book
        author (str): Author of the book
        genre (str): Genre of the book
        ISBN (str): ISBN of the book
        """
        self._title = title
        self._author = author
        self._genre = genre
        self._ISBN = ISBN
        self._status = 'available'
        self._borrower = None

    @property
    def title(self):
        """
        Returns the title of the Book object
        """
        return self._title

    @title.setter
    def title(self, value):
        """
        Sets the title of the Book object

        Args:
        value (str): Title of the book
        """
        self._title = value

    @property
    def author(self):
        """
        Returns the author of the Book object
        """
        return self._author

    @author.setter
    def author(self, value):
        """
        Sets the author of the Book object

        Args:
        value (str): Author of the book
        """
        self._author = value

    @property
    def genre(self):
        """
        Returns the genre of the Book object
        """
        return self._genre

    @genre.setter
    def genre(self, value):
        """
        Sets the genre of the Book object

        Args:
        value (str): Genre of the book
        """
        self._genre = value

    @property
    def ISBN(self):
        """
        Returns the ISBN of the Book object
        """
        return self._ISBN

    @ISBN.setter
    def ISBN(self, value):
        """
        Sets the ISBN of the Book object

        Args:
        value (str): ISBN of the book
        """
        self._ISBN = value

    @property
    def status(self):
        """
        Returns the status of the Book object
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the status of the Book object

        Args:
        value (str): Status of the book
        """
        self._status = value

    @property
    def borrower(self):
        """
        Returns the borrower of the Book object
        """
        return self._borrower

    @borrower.setter
    def borrower(self, value):
        """
        Sets the borrower of the Book object

        Args:
        value (str): Borrower of the book
        """
        self._borrower = value

    def borrow(self, borrower):
        """
        Borrows a book and assigns the borrower

        Args:
        borrower (str): name of the borrower
        """
        self.status = 'borrowed'
        self.borrower = borrower

    def return_book(self):
        """
        Returns a book and removes the borrower
        """
        self.status = 'available'
        self.borrower = None


class User:
    """
    Represents a user of the library with a name and email address
    """

    def __init__(self, name, email):
        """
        Initializes a new User object with the given attributes

        Args:
        name (str): Name of the user
        email (str): Email address of the user
        """
        self._name = name
        self._email = email

    @property
    def name(self):
        """
        Returns the name of the User object
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the name of the User object

        Args:
        value (str): Name of the user
        """
        self._name = value

    @property
    def email(self):
        """
        Returns the email address of the User object
        """
        return self._email

    @email.setter
    def email(self, value):
        """
        Sets the email address of the User object

        Args:
        value (str): Email address of the user
        """
        self._email = value


class Library:
    """
    Represents a library of books and users
    """

    def __init__(self):
        """
        Initializes a new Library object with an empty list of Books and users
        """
        self.books = []
        self.users = []

    def addBook(self, book):
        """
        Adds a Book to the Library

        Args:
        book (Book): The Book object to add to the Library
        """
        self.books.append(book)

    def deleteBook(self, ISBN):
        """
        Deletes a Book from the Library using its ISBN

        Args:
        ISBN (str): The ISBN of the Book to delete
        """
        for book in self.books:
            if book.ISBN == ISBN:
                self.books.remove(book)

    def displayAllBooks(self):
        """
        Displays all the Books in the Library
        """
        for book in self.books:
            print(f'Title: {book.title}, Author: {book.author}, Genre: {book.genre}, ISBN: {book.ISBN}, Status: {book.status}, Borrower: {book.borrower}')

    def searchByTitle(self, title):
        """
        Searches for a Book by its title

        Args:
        title (str): The title of the Book to search for

        Returns:
        A list of matching books
        """
        matching_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                matching_books.append(book)
        return matching_books

    def searchByAuthor(self, author):
        """
        Searches for books by an author

        Args:
        author (str): The author to search for

        Returns:
        A list of matching books
        """
        matching_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                matching_books.append(book)
        return matching_books

    def saveBooksToFile(self, filename):
        """
        Saves the books to a CSV file

        Args:
        filename (str): The name of the CSV file
        """
        with open(filename, "w") as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            header = ["title", "author", "genre", "ISBN", "status", "borrower"]
            writer.writerow(header)
            for book in self.books:
                writer.writerow([book.title, book.author, book.genre, book.ISBN, book.status, book.borrower])

    def loadBooksFromFile(self, filename):
        """
        Loads books from a CSV file

        Args:
        filename (str): The name of the CSV file

        Returns:
        A list of Books
        """
        with open(filename, "r") as file:
            reader = csv.reader(file)
            # Skip the header row
            next(reader)
            for row in reader:
                book = Book(row[0], row[1], row[2], row[3])
                book.status = row[4]
                book.borrower = row[5]
                self.addBook(book)

    def getUserByEmail(self, email):
        """
        Retrieves a User object by their email address

        Args:
        email (str): The email address of the user to retrieve

        Returns:
        The User object, or None if not found
        """
        for user in self.users:
            if user.email.lower() == email.lower():
                return user
        return None

    def addUser(self, user):
        """
        Adds a User to the Library

        Args:
        user (User): The User object to add to the Library
        """
        self.users.append(user)

    def getCheckedOutBooksByUser(self, user):
        """
        Retrieves a list of Books that are checked out by a particular user

        Args:
        user (User): The User object to retrieve checked out books for

        Returns:
        A list of checked out Books
        """
        checked_out_books = []
        for book in self.books:
            if book.borrower:
                if book.borrower.email.lower() == user.email.lower():
                    checked_out_books.append(book)
        return checked_out_books

    def generateBookReport(self):
        """
        Generates an inventory report of the Library's books
        """
        num_books = len(self.books)
        print(f'Total number of books: {num_books}')
        genres = set([book.genre for book in self.books])
        for genre in genres:
            num_genre_books = len([book for book in self.books if book.genre.lower() == genre.lower()])
            print(f'{genre} books: {num_genre_books}')

    def generateUserReport(self):
        """
        Generates a report of all Library users and their checked out books
        """
        for user in self.users:
            print(f'User: {user.name}, Email: {user.email}')
            checked_out_books = self.getCheckedOutBooksByUser(user)
            if len(checked_out_books) == 0:
                print('No checked out books')
            else:
                for book in checked_out_books:
                    print(f'Book: {book.title}, Author: {book.author}, ISBN: {book.ISBN}')




"""
This UserInterface class has the following methods:

displayMenu(): Displays a menu of operation options for the user to select.

executeChoice(choice): Executes a specific library operation based on the user's selection from the menu.

run(): Continuously displays the menu and gets user input until the user chooses to exit the application.

"""
class UserInterface:
    def __init__(self, library):
        self.library = library

    def displayMenu(self):
        menu = 'Library Management System\n\n'
        menu += '1. Add Book\n'
        menu += '2. Delete Book\n'
        menu += '3. Display All Books\n'
        menu += '4. Search by Title\n'
        menu += '5. Search by Author\n'
        menu += '6. Borrow Book\n'
        menu += '7. Return Book\n'
        menu += '8. Generate Book Report\n'
        menu += '9. Generate User Report\n'
        menu += 'X. Exit\n'
        print(menu)

    def executeChoice(self, choice):
        if choice == '1':
            title = input('Enter the title: ')
            author = input('Enter the author: ')
            genre = input('Enter the genre: ')
            ISBN = input('Enter the ISBN: ')
            book = Book(title, author, genre, ISBN)
            self.library.addBook(book)
            print('Book added successfully.')

        elif choice == '2':
            ISBN = input('Enter the ISBN of the book to delete: ')
            self.library.deleteBook(ISBN)
            print('Book deleted successfully.')

        elif choice == '3':
            self.library.displayAllBooks()

        elif choice == '4':
            title = input('Enter the title to search for: ')
            matching_books = self.library.searchByTitle(title)
            if len(matching_books) == 0:
                print('No matching books found.')
            else:
                print(f'{len(matching_books)} matching books found:')
                for book in matching_books:
                    print(f'{book.title} by {book.author}')

        elif choice == '5':
            author = input('Enter the author to search for: ')
            matching_books = self.library.searchByAuthor(author)
            if len(matching_books) == 0:
                print('No matching books found.')
            else:
                print(f'{len(matching_books)} matching books found:')
                for book in matching_books:
                    print(f'{book.title} by {book.author}')

        elif choice == '6':
            email = input('Enter your email address: ')
            user = self.library.getUserByEmail(email)
            if not user:
                print('User not found.')
                return
            ISBN = input('Enter the ISBN of the book to borrow: ')
            book = self.library.searchByISBN(ISBN)
            if not book:
                print('Book not found.')
                return
            if book.status == 'borrowed':
                print('Book already borrowed.')
                return
            book.borrow(user)
            print(f'{book.title} borrowed successfully by {user.name}.')

        elif choice == '7':
            ISBN = input('Enter the ISBN of the book to return: ')
            book = self.library.searchByISBN(ISBN)
            if not book:
                print('Book not found.')
                return
            if book.status == 'available':
                print('Book already returned.')
                return
            book.return_book()
            print(f'{book.title} returned successfully.')

        elif choice == '8':
            self.library.generateBookReport()

        elif choice == '9':
            self.library.generateUserReport()

        elif choice == 'X':
            return

        else:
            print('Invalid choice.')

    def run(self):
        while True:
            self.displayMenu()
            choice = input('Enter your choice: ')
            self.executeChoice(choice)
            if choice == 'X':
                break


"""
n this Main class, we simply create
 a Library object and a UserInterface 
 object with that library object as its 
 parameter, then call run() on the UserInterface 
 object. When the user chooses to exit from the 
 UserInterface class, the program ends.
"""
class Main:
    def main(self):
        library = Library()
        ui = UserInterface(library)
        ui.run()
