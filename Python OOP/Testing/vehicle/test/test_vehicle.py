import unittest

from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def test_init__expect_to_initialize_correctly(self):
        vehicle = Vehicle(100, 120)
        self.assertEqual(vehicle.fuel, 100)
        self.assertEqual(vehicle.horse_power, 120)
        self.assertEqual(vehicle.capacity, 100)
        self.assertEqual(vehicle.fuel_consumption, 1.25)

    def test_drive__when_expect_to_raise(self):
        vehicle = Vehicle(100, 120)
        with self.assertRaises(Exception) as ex:
            vehicle.drive(vehicle.fuel)

        self.assertIsNotNone(ex)
        expected_message = "Not enough fuel"
        self.assertEqual(expected_message, str(ex.exception))

    def test_drive__when_expect_to_be_correct(self):
        vehicle = Vehicle(100, 120)
        vehicle.drive(20)
        self.assertEqual(vehicle.fuel, 75)

    def test_refuel__when_expect_to_raise(self):
        vehicle = Vehicle(100, 120)
        with self.assertRaises(Exception) as ex:
            vehicle.refuel(vehicle.fuel + 1)

        self.assertIsNotNone(ex)
        expected_message =  "Too much fuel"
        self.assertEqual(expected_message, str(ex.exception))

    def test_refuel__when_expect_to_be_correct(self):
        vehicle = Vehicle(100, 120)
        vehicle.drive(20)
        vehicle.refuel(10)
        self.assertEqual(vehicle.fuel, 85)

    def test_str__expect_to_output_proper_message(self):
        vehicle = Vehicle(100, 120)
        expected_message = f"The vehicle has {vehicle.horse_power} " \
               f"horse power with {vehicle.fuel} fuel left and {vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(expected_message, str(vehicle))

