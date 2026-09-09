import json

class Book:
    def __init__(self,title,Aurthor,ISBN):
        self.title = title
        self.Aurthor = Aurthor
        self.ISBN = ISBN
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"Title: {self.title} || Aurthor: {self.Aurthor} || ISBN: {self.ISBN} || {status}"

class EBook(Book):
    def __init__(self, title, Aurthor, ISBN,file_size):
        super().__init__(title, Aurthor, ISBN)
        self.file_size = file_size



class PhysicalBook(Book):
    def __init__(self, title, Aurthor, ISBN,Physical_Location):
        super().__init__(title, Aurthor, ISBN)
        self.Physical_Location = Physical_Location


class Library:
    def __init__(self):
        self.books = []

    def add_books(self,book):
        self.books.append(book)
        print("Book Added Successfully")

    def view_books(self):
        if(len(self.books) == 0):
            print("List is empty")
        else:
            for i in self.books:
                print(i)

    def issue_book(self,ISBN):
        for i in self.books:
            if(ISBN == i.ISBN):
                if i.available == True:
                    i.available = False
                    print("Book Issue Successfully")
                else:
                    print("Book Already Issued")
                return 
        print("Book Not Found")

    def return_book(self,ISBN):
        for i in self.books:
            if(ISBN == i.ISBN):
                if i.available == False:
                    i.available = True
                    print("Book Returned Sucessfully")
                else:
                    print("Book Not Returned")
                return
        print("Book Not Found")


    def save_to_file(self):
        data = []
        for i in self.books:
            if isinstance(i,EBook):
                book_dict={"type": "Ebook","title":i.title,"Aurthor": i.Aurthor,"ISBN":i.ISBN,"Available": i.available,"File_size": i.file_size}
            else:
                book_dict={"type": "PhysicalBook","title":i.title,"Aurthor":i.Aurthor,"ISBN":i.ISBN,"Available": i.available,"PhysicalLocation": i.Physical_Location}

            data.append(book_dict)

        with open("Library.json","w")as f:
            json.dump(data,f)
        print("Data save succesfully")

    def load_from_file(self):
        try:
            with open("Library.json","r")as f:
                data = json.load(f)
            for i in data:
                if(i["type"]== "Ebook"):
                    new = EBook(i["title"],i["Aurthor"],i["ISBN"],i["File_size"])
                else:
                    new = PhysicalBook(i["title"],i["Aurthor"],i["ISBN"],i["PhysicalLocation"])
                new.available = i["Available"]
                self.books.append(new)
            print("Loaded Successfully")
        except FileNotFoundError:
            print("No Save File Found")
            


library = Library()
library.load_from_file()
while True:
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Books")
    print("4. Return Books")
    print("5. Save & Exit")

    choice = input("Enter Your Choice: ")
    if(choice == "1"):
        title= input("Enter Title of Book: ")
        Aurthor = input("Enter the Aurthor name: ")
        ISBN = input("Enter the code of book: ")
        n = input("1. for EBook, 2. for Physical Book : ")
        if(n == "1"):
            file_size = input("Enter file size: ") 
            newBook= EBook(title,Aurthor,ISBN, file_size)
        else:
            Physical_Location = input("Enter shelf location: ")  
            newBook = PhysicalBook(title,Aurthor,ISBN,Physical_Location)
        library.add_books(newBook)

    elif(choice == "2"):
        library.view_books()
    elif(choice == "3"):
        ISBN = input("Enter Book Code for Issueing: ")
        library.issue_book(ISBN)
    elif(choice == "4"):
        ISBN = input("Enter Book Code for returning: ")
        library.return_book(ISBN)
    elif(choice == "5"):
        library.save_to_file()
        print("Good Bye")
        break
    else:
        print("Invalid input")



