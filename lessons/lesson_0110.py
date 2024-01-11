# CLASS PRACTICE AGAIN
class Book:
    def __init__(self, my_title, my_author, my_language, my_price, my_rating, my_genre):
        self.title = my_title
        self.author = my_author
        self.language = my_language
        self.price = my_price
        self.rating = my_rating
        self.genre = my_genre
        self.readers = 0

    def introduce_book(self):
        return f"{self.title} is a {self.genre} book that is written by {self.author}."

    def is_expensive(self):
        output = False
        if self.price >= 2000:
            output = True
        return output

    def change_rating(self):
        new_rating = input("Rate the book out of 5 stars: ")
        while new_rating not in "12345":
            new_rating = input("Rate the book out of 5 stars: ")
        self.rating = new_rating
        return "Your rating has been changed."

    def add_completion(self):
        self.readers += 1


may_favorite_book = Book("Wolf by Wolf", "Ryan Gosling", "English", "1000", 5, "Science Fiction")
yuiko_favorite_book = Book("Little Prince", "Saint-Ex", "French", "500", 5, "children")

print(may_favorite_book.introduce_book())
print(may_favorite_book.change_rating())

