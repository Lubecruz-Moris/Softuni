

from lab.car_manager import Car
import unittest

class CarManagerTests(unittest.TestCase):
    def test_innit__make_initialization__expect_to_be_correct(self):
        car = Car("a", "b", 1, 4)
        expected_make = 'a'
        expected_model = 'b'
        expected_fuel_consumption = 1
        expected_fuel_capacity = 4
        self.assertEqual(car.make, expected_make)
        self.assertEqual(car.model, expected_model)
        self.assertEqual(car.fuel_consumption, expected_fuel_consumption)
        self.assertEqual(car.fuel_capacity, expected_fuel_capacity)

    def test_make_expect_to_raise(self):

        with self.assertRaises(Exception) as ex:
            car = Car("", "b", 1, 4)
        self.assertIsNotNone(ex)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_expect_to_raise(self):

        with self.assertRaises(Exception) as ex:
            car = Car("a", "", 1, 4)
        self.assertIsNotNone(ex)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_expect_to_raise(self):

        with self.assertRaises(Exception) as ex:
            car = Car("a", "b", 0, 4)
        self.assertIsNotNone(ex)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_expect_to_raise(self):

        with self.assertRaises(Exception) as ex:
            car = Car("a", "b", 1, 0)
        self.assertIsNotNone(ex)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_expect_to_raise(self):
        car = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -1
        self.assertIsNotNone(ex)
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount_expect_to_be_correct(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual(car.fuel_amount, 0)

    def test_refuel_expect_to_raise_with_negative_values(self):
        car = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            car.refuel(0)

        self.assertIsNotNone(ex)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_when_expect_to_be_correct(self):
        car = Car("a", "b", 1, 4)
        car.refuel(1)
        self.assertEqual(car.fuel_amount, 1)

    def test_refuel_when_capacity_reach(self):
        car = Car("a", "b", 1, 4)
        car.refuel(5)
        self.assertEqual(car.fuel_capacity, car.fuel_amount)
    def test_drive_when_expect_to_raise(self):
        car = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            car.drive(500)
        self.assertIsNotNone(ex)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_when_expect_to_be_correct(self):
        car = Car("a", "b", 2, 10)
        car.refuel(2)
        car.drive(50)
        self.assertEqual(car.fuel_amount, 1)


if __name__ == '__main__':
    unittest.main()
