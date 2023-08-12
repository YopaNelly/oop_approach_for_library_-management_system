# OOP Approach for Library Management System
This project is a Library Management System implemented using object-oriented programming principles in Python. The project includes three classes, Book, Library, and UserInterface, and a Main class with the main() method to start the application.

## Book Class:
The Book class represents a book in the library, with the following attributes:

`title (string)`
`author (string)`
`genre (string)`
`ISBN (string)`
The class also includes getter and setter methods for each attribute.

## Library Class:
The Library class represents the library itself, with the following attributes and methods:

books (list): An empty list to store Book objects.
addBook(book: Book): Adds a Book object to the library.
deleteBook(ISBN: string): Deletes a book from the library based on its ISBN.
searchByTitle(title: string): list: Searches for books in the library by title and returns a list of matching books.
searchByAuthor(author: string): list: Searches for books in the library by author and returns a list of matching books.
displayAllBooks(): Displays all the books in the library.
saveBooksToFile(filename: string): Saves the book data from the library to a file.
loadBooksFromFile(filename: string): Loads book data from a file and populates the library with the data.
The Library class also includes additional functionality for book borrowing and returning, calculating book statistics, generating book reports, and managing user information.

## UserInterface Class:
The UserInterface class provides a menu-driven interface for users to interact with the library system, with the following methods:

displayMenu(): Displays the menu options for the user to choose from.
executeChoice(choice: string): Handles user inputs and calls the appropriate methods in the Library class based on the user's choice.
run(): Continuously displays the menu and handles user interactions until the user chooses to exit the application.
## Main Class:
The Main class serves as the entry point for the program, with the main() method to start the library management system.

## Future Improvements:
Add user authentication to restrict access to certain library functions.
Implement a loan system that can track the due dates of borrowed books.
Add a graphical user interface to interact with the system.