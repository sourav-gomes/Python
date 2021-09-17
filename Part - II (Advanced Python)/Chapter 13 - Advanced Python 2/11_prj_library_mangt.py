class Library:

    def __init__(self, listOfBooks):    # constructor -> initialises the object
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books available now: \n")
        for i, book in enumerate(self.books):
            print(f"  {i+1}. {book}")

    def borrowBooks(self, bookName):
        if bookName in self.books:
            print(f"The book '{bookName}' has been issued to you. Kindly return it within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, this book is either issued/unavailable at present.")
            return False
    
    def returnBooks(self, bookName):
        if bookName in self.books:
            print(f"The book '{bookName}' issued to you, has now been returned. Hope you enjoyed it. :)")
            self.books.append(bookName)
        else:
            print(f"The new book has been added. Thank you!")
            self.books.append(bookName)

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the Book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the Book you want to return: ")
        return self.book    

if __name__ == "__main__":
    centralLibrary = Library(["Python", "Learn C++", "Basics of HTML", "Cloud Computing"])    # instantiating the object
    centralLibrary.displayAvailableBooks()
    
    student = Student()

    while(True):
        mainMenu = '''


        \t===== CENTRAL LIBRARY MAIN MENU =====\n
        \tPlease choose an option (1-4):\n
        \t1. List all available books
        \t2. Request a book
        \t3. Return/Add a book
        \t4. Exit the Menu

        '''
        print(mainMenu)

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            centralLibrary.displayAvailableBooks()
        elif choice == 2:
            centralLibrary.borrowBooks(student.requestBook())
        elif choice == 3:
            centralLibrary.returnBooks(student.returnBook())
        elif choice == 4:
            print("Thanks for choosing Central Library. Have a great day!")
            exit()
        else:
            print("Invalid choice. (Hint: Choose a number between 1-4)")





