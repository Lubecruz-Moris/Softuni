from project.library import Library
import unittest

class LibraryTests(unittest.TestCase):
    def test_init__initialization(self):
        library = Library("Library")
        self.assertEqual(library.name, "Library")
        self.assertEqual(library.readers, {})
        self.assertEqual(library.books_by_authors, {})

    def test_name__when_empty_or_None_expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            library = Library("")

        self.assertIsNotNone(ex.exception)
        expected_message = "Name cannot be empty string!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_add_book__expect_to_be_correct(self):
        library = Library("Library")
        library.add_book("Author", "Title")
        expected_result = {"Author": ["Title"]}
        self.assertDictEqual(library.books_by_authors,expected_result)
    def test_add_book

