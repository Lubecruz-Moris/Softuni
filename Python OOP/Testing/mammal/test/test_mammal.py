import unittest

from project.mammal import Mammal


class MammalTests(unittest.TestCase):
    NAME = "Pesho"
    TYPE = "Dog"
    SOUND = "Woof"
    KINGDOM = 'animals'

    def setUp(self) -> None:
        self.mammal = Mammal(self.NAME, self.TYPE, self.SOUND)

    def test_init__expect_correct_initialization(self):
        self.assertEqual(self.mammal.name, "Pesho")
        self.assertEqual(self.mammal.type, "Dog")
        self.assertEqual(self.mammal.sound, "Woof")
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_make_sound_expect_to_be_correct(self):
        expected_message = "Pesho makes Woof"
        self.assertEqual(self.mammal.make_sound(), expected_message)
    def test_info_expect_to_be_correct(self):
        expected_message = "Pesho is of type Dog"
        self.assertEqual(self.mammal.info(), expected_message)