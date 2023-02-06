from lab.list import IntegerList
import unittest


class ListTests(unittest.TestCase):
    def index_out_of_range(self, func_ref):
        data = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ex:
            func_ref(3)

        self.assertIsNotNone(ex)
        expected_message = "Index is out of range"
        return self.assertEqual(ex.exception.args[0], expected_message)

    def test__innit__expect_to_take_only_integers(self):
        data = IntegerList(1, 'a', 2)
        expected_result = [1, 2]
        self.assertEqual(data.get_data(), expected_result)

    def test__add__expect_to_add_an_integer_to_the_list(self):
        data = IntegerList(1, 2, 3)
        data.add(1)
        result = data.get_data()
        self.assertEqual(result, [1, 2, 3, 1])

    def test__remove_index__expect_to_remove_an_integer_on_the_given_index(self):
        data = IntegerList(1, 2, 3)
        data.remove_index(0)
        result = data.get_data()
        self.assertEqual(result, [2, 3])

    def test__get__expect_to_return_element_on_the_given_index(self):
        data = IntegerList(1, 2, 3)
        expected_result = data.get(1)
        self.assertEqual(2, expected_result)

    def test__insert__expect_to_insert_element_on_the_given_index(self):
        data = IntegerList(1, 2, 3)
        data.insert(0, 3)
        self.assertEqual(data.get_data(), [3,1,2,3])


    def test__get_biggest__expect_to_get_element_with_highest_value(self):
        data = IntegerList(1, 2, 3)
        expected_result = 3
        self.assertEqual(data.get_biggest(), expected_result)

    def test__get_index__expect_to_return_index_of_given_element(self):
        data = IntegerList(1, 2, 3)
        expected_result = data.get_index(1)
        self.assertEqual(0, expected_result)

    def test__remove_index__expect_to_raise_IndexError(self):
        data = IntegerList(1, 2, 3)
        self.index_out_of_range(data.remove_index)

    def test__get__expect_to_raise_IndexError(self):
        data = IntegerList(1, 2, 3)
        self.index_out_of_range(data.get)

    def test__insert__expect_to_raise_IndexError(self):
        data = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ex:
            data.insert(3, 1)

        self.assertIsNotNone(ex)
        expected_message = "Index is out of range"
        self.assertEqual(ex.exception.args[0], expected_message)

    def test__insert_expect_to_raise_ValueError(self):
        data = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as ex:
            data.insert(1, 'a')

        self.assertIsNotNone(ex)
        expected_message = "Element is not Integer"
        self.assertEqual(ex.exception.args[0], expected_message)

    def test__add__invalid_type__expect__to_raise_ValueError(self):
        data = IntegerList(1, 2, 3)

        with self.assertRaises(ValueError) as ex:
            data.add('a')

        self.assertIsNotNone(ex)
        expected_message = "Element is not Integer"
        self.assertEqual(ex.exception.args[0], expected_message)


if __name__ == '__main__':
    unittest.main()
