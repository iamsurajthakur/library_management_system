class Library:

    def __init__(self, lst, name):
        self.bookList = lst
        self.name = name
        self.lendDict = {}

    def addbook(self,book):
        self.bookList.append(book)
        print('Book has been added to the book list')

    def displaybook(self):
        print(f'We have the following books in our library: {self.name}')
        for book in self.bookList:
            print(book)

    def bookended(self):
        if len(self.lendDict) == 0:
            print('No books lended')
        else:
            print('-----The following are the books lended-----')
            for bok in self.lendDict:
                print(bok)
    def lend(self,book,user):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print('Book dictionary has been updated')
        else:
            print(f'Book is already occupied by {self.lendDict[book]}')

    def returnbook(self, book):
        if book in self.lendDict.keys():
            del self.lendDict[book]
            print(f"The book {book} has been returned.")
        else:
            print(f"There is no book named {book} taken from our library.")


if __name__ == '__main__':
    library = Library(['python', 'c++', 'java', 'ruby', 'os'], 'ilios')

    while True:
        print(f'Welcome to {library.name} library. Enter your choice')
        print('1. Display Book')
        print('2. Lend a book')
        print('3. Return a book')
        print('4. Add a book')
        print('5. Display lended book')
        userChoice = int(input('Enter your choice:'))

        if userChoice == 1:
            library.displaybook()

        elif userChoice == 2:
            book = input('Enter the name of your book:')
            book = book.title()
            name = input('Enter your full name:')
            name = name.title()
            library.lend(book, name)

        elif userChoice == 3:
            book = input('Enter the name of your book:')
            book = book.title()
            library.returnbook(book)

        elif userChoice == 4:
            book = input('Enter the name of your book:')
            book = book.title()
            library.addbook(book)

        elif userChoice == 5:
            library.bookended()

        else:
            print('Not a valid number')

        print('----Enter q to quit or any other key to continue----')
        choice = input('->')


        if choice == 'q':
            exit()
        elif choice == 'c':
            continue