## HW 9 pt1 DS5100

import pandas as pd 
import numpy as np

class BookLover:
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        self.book_name = book_list["book_name"]
        self.book_rating = book_list["book_rating"] ## not sure here
    
    def add_book(self, book_name, book_rating):
        if book_name not in self.book_list:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [book_rating]
                })

            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        else:
            return print("there already exists an entry with the same name")

    def has_read(self, book_name):
        x1 = str(self.books()["book_name"])
        if (book_name in x1):
            return True
        else:
            return False
    
    def num_books_read(self):
        num = len(self.book_list)
        return num

    def fav_books(self):
        fav = self.book_list[self.book_list['book_rating'] > 3]
        return fav
    
    def books(self):
        return self.book_list

