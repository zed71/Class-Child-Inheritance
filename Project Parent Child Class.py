# Parent Class Book
class Book:
    name = "J.R.R. Tolkein"
    title = "The Hobbit"
    published = 1957

    def getInformation(self):
        genre = input("What is the genre of the book: ")
        publisher = input("Who published the book: ")
        copyright_date = input("What is the year of copyright: ")
        if (publisher == name.publisher and copyright_date == name.copyright_date):
            print("Here is the book genre, {}!".format(genre))
        else:
            print("That's not the book.")

# Child Class Writer
class Writer(Book):
    year_written = 1957
    series_type = "Fantasy"


    def getInformation(self):
        genre = input("What is the genre of the book: ")
        publisher = input("Who published the book: ")
        copyright_month_date = input("Enter the month and date of copyright: ")
        if (publisher == name.publisher and copyright_date == name.copyright_month_date):
            print("Here is the book genre, {}!".format(genre))
        else:
            print("That's not the book.")

class Genre(Book):
    age_group = "adult"
    series = "star wars"


    def getInformation(self):
        genre = input("What is the genre of the book: ")
        publisher = input("Who published the book: ")
        copyright_month_date = input("Enter the month and date of copyright: ")
        if (publisher == name.publisher and copyright_date == name.copyright_month_date):
            print("Here is the book genre, {}!".format(genre))
        else:
            print("That's not the book.")

       
#The following code invokes the methods inside each class for Book and Writer.
        
book = Book()
book.getInformation()

writer = Writer()
writer.getInformation() 
