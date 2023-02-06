import os
import unittest

from project.bookstore import Bookstore

class BookstoreTests(unittest.TestCase):

    def test_init_when_correct(self):
        book = Bookstore(5)
        self.assertEqual(book.books_limit, 5)
        self.assertEqual(book.availability_in_store_by_book_titles, {})
        self.assertEqual(book.total_sold_books, 0)

    def test_init_when_value_error_expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            book = Bookstore(0)
        expected_message = f"Books limit of 0 is not valid"
        self.assertIsNotNone(ex.exception)
        self.assertEqual(expected_message, str(ex.exception))

    def test_init_when_value_error_negative_expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            book = Bookstore(-1)
        expected_message = f"Books limit of -1 is not valid"
        self.assertIsNotNone(ex.exception)
        self.assertEqual(expected_message, str(ex.exception))

    def test_receive_book_expect_to_be_correct(self):
        book = Bookstore(5)
        result = book.receive_book("The shining", 2)
        expected = f"2 copies of The shining are available in the bookstore."
        self.assertEqual(expected, result)
        self.assertDictEqual(book.availability_in_store_by_book_titles,{"The shining" : 2})


    def test_len_expect_to_be_correct(self):
        book = Bookstore(5)
        book.receive_book("The shining", 2)
        result = len(book)
        self.assertEqual(result, 2)

    def test_receive_book_when_book_already_added(self):
        book = Bookstore(5)
        result_first = book.receive_book("The shining", 1)
        result_second = book.receive_book("The shining", 1)
        expected_first = f"1 copies of The shining are available in the bookstore."
        expected_second = f"2 copies of The shining are available in the bookstore."
        self.assertEqual(expected_first, result_first)
        self.assertEqual(expected_second, result_second)
        self.assertDictEqual(book.availability_in_store_by_book_titles, {"The shining": 2})

    def test_receive_book_when_book_limit_reached_expect_to_raise(self):
        book = Bookstore(1)
        with self.assertRaises(Exception) as ex:
            book.receive_book("The shining", 2)

        self.assertIsNotNone(ex.exception)
        expected_message = "Books limit is reached. Cannot receive more books!"

        self.assertEqual(expected_message, str(ex.exception))



    def test_sell_book_when_not_available_expect_to_raise(self):
        book = Bookstore(1)
        with self.assertRaises(Exception) as ex:
            book.sell_book("The shining", 2)
        expected = f"Book The shining doesn't exist!"
        self.assertIsNotNone(ex.exception)
        self.assertEqual(expected,str(ex.exception))

    def test_sell_book_when_insufficient_copies_expect_to_raise(self):
        book = Bookstore(1)
        book.receive_book("The shining", 1)
        with self.assertRaises(Exception) as ex:
            book.sell_book("The shining", 2)
        self.assertIsNotNone(ex.exception)
        expected = f"The shining has not enough copies to sell. Left: 1"
        self.assertEqual(expected, str(ex.exception))

    def test_sell_book_expect_to_be_correct(self):
        book = Bookstore(2)
        book.receive_book("The shining", 2)
        result = book.sell_book("The shining", 2)
        expected = f"Sold 2 copies of The shining"
        self.assertEqual(result, expected)
        self.assertEqual(book.total_sold_books, 2)
        self.assertEqual(book.availability_in_store_by_book_titles, {"The shining": 0})
    def test_str_expect_to_be_correct(self):
        book = Bookstore(2)
        book.receive_book("The shining", 2)
        book.sell_book("The shining", 1)
        expected = f"Total sold books: {book.total_sold_books}" + "\n"
        expected += f'Current availability: {len(book)}' + "\n"
        expected += " - The shining: 1 copies"
        self.assertEqual(str(book), expected)

