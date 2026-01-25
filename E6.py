class library:
    def __init__(self):
        self.books=[]
        self.no_of_books=0

    def add_book(self,book_name):
        self.books.append(book_name)
        self.no_of_books +=1
        print(f"'{book_name}' added successfully.")

    def remove_book(self,book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            self.no_of_books -=1
            print(f"'{book_name}' removed successfully.") 
        else:
            print("'{book_name}' not found!")   

    def display_books(self):
        print("\nBooks in library")
        for book in self.books:
            print("-" + book)
        print("Total books:", self.no_of_books)    

my_library=library()

my_library.add_book("Intro to Python")
my_library.add_book("Intro to JAVA")
my_library.add_book("Intro to C")
my_library.add_book("Intro to C++")
my_library.add_book("Intro to Html-5")
my_library.display_books()