from lab.worker import Worker
import unittest




class WorkerTests(unittest.TestCase):
    def test__innit__values_if_initialized_correctly(self):
        worker = Worker('Lubo', 1024, 1)

        expected_name = 'Lubo'
        expected_salary = 1024
        expected_energy = 1
        expected_money = 0

        self.assertEqual(worker.name, expected_name)
        self.assertEqual(worker.salary, expected_salary)
        self.assertEqual(worker.energy, expected_energy)
        self.assertEqual(worker.money, expected_money)

    def test__rest__when_called__energy_incremented_correctly(self):
        worker = Worker('Lubo', 1024, 1)
        initial_energy = worker.energy
        worker.rest()
        self.assertEqual(initial_energy + 1, worker.energy)

    def test__work__when_called_with_invalid_energy_expected_to_raise(self):
        worker = Worker('Lubo', 1024, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        expected_message = 'Not enough energy.'
        self.assertEqual(ex.exception.args[0], expected_message)
    def test__work__when_called_expect_money_to_increase_by_salary(self):
        worker = Worker('Lubo', 1024, 2)
        worker.work()
        worker.work()
        self.assertEqual(2 * worker.salary, worker.money)

    def test__work__when_called__expect_energy_to_decrement(self):
        worker = Worker('Lubo', 1024, 1)
        initial_energy = worker.energy
        worker.work()
        self.assertEqual(initial_energy - 1, worker.energy)

    def test__get_info__return__expect_correct_values(self):
        worker = Worker('Lubo', 1024, 1)
        expected_result = f'Lubo has saved 0 money.'
        actual_info = worker.get_info()
        self.assertEqual(actual_info, expected_result)


if __name__ == '__main__':
    unittest.main()
