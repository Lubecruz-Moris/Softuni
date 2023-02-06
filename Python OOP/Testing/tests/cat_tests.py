from lab.cat import Cat
import unittest




class CatTests(unittest.TestCase):
    NAME = "Chelsea"
    def setUp(self) -> None:
        self.cat = Cat(self.NAME)
    def test__eat__expect_size_increase(self):
        initial_size = self.cat.size
        self.cat.eat()
        self.assertEqual(initial_size + 1, self.cat.size)
    def test__eat__expect_fed_to_be_true_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test__eat__when_fed_is_True_expect_to_raise(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertIsNotNone(ex)
    def test__sleep__when_fed_is_False_expect_to_raise(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertIsNotNone(ex)

    def test__sleep__expect_sleepy_as_False(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)



if __name__ == '__main__':
    unittest.main()