# part 2
import unittest
import pandas as pd
import numpy as np

from BookLover import BookLover


class BookLoverTestSuite:

    def test_1_add_book(self):
        test1 = BookLover("Test", "Test@Test.com", "Test")
        test1.add_book("Test Book", 4)
        return BookLover.has_read(test1, "Test Book")

    def test_2_add_book(self):
        test2 = BookLover("Test", "Test@Test.com", "Test")
        test2.add_book("Test Book 1", 4)
        test2.add_book("Test Book 1", 4)
        x = BookLover.books(test2)["Test Book 1"]
        return len(x)

    def test_3_has_read(self):
        test3 = BookLover("test", "test email", "test")
        test3.add_book("test book", 3)
        x = test3.books()["book_name"]
        if ("test book" in x):
            return True
        else:
            return False 
            
    def test_4_has_read(self):
        test4 = BookLover("test", "test email", "test")
        test4.add_book("test book", 4)
        book = test4.books()
        return test4.assertFalse(test4, book)

    def test_5_num_books_read(self):
        test5 = BookLover("test", "test email", "test")
        test5.add_book("test book", 4)
        test5.add_book("test book1", 4)
        return test5.num_books() == 2

    def test_6_fav_books(self):
        test6 = BookLover("test", "test email", "test")
        test6.add_book("test book", 4)
        test6.add_book("test book1", 2)
        return test6.fav_books

if __name__ == '__main__':
    
    unittest.main(verbosity=3)