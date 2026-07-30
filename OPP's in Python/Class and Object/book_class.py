# Create a simple book class with with basic attributes
# Practice : Create the class then create 3 book objects



## Class creation
class Book:

    # Data attribute
    def __init__(self, title , author ,pages ):
        self.title = title
        self.author = author
        self.pages = pages

    # Function attribute
    def get_info(self):
        return f" author : {self.author}, Title : {self.title}, Pages : {self.pages}"
        

# object Creation

book1 = Book("The Alchemist",'Paulo Coelho',208)
book2 = Book('To Kill a Mockingbird','Harper Lee',281)
book3 = Book("Harry Potter and the Sorcerer's Stone",'J.K. Rowling',309)

# Object calling

print(book1.get_info())
print(book2.get_info())
print(book3.get_info())
    