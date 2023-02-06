import unittest

from project.student import Student


class StudentTests(unittest.TestCase):
    def test_init__when_courses_is_empty(self):
        student = Student("Student", dict())
        self.assertEqual(student.name, "Student")
        self.assertEqual(student.courses, {})

    def test_init__when_courses_is_filled(self):
        student = Student("Student", {"Python Basics": []})
        self.assertEqual(student.name, "Student")
        self.assertEqual(student.courses, {"Python Basics": []})

    def test_init__when_courses_is_filled_with_notes(self):
        student = Student("Student", {"Python Basics": ['note 1']})
        self.assertEqual(student.name, "Student")
        self.assertEqual(student.courses, {"Python Basics": ['note 1']})

    def test_enroll__when_course_already_exists(self):
        course_name = "Python Basics"
        student = Student("Student", {course_name: ['note 1']})

        result = student.enroll(course_name, ['note 2', 'note 3'], 'Y')
        expected_notes = ['note 1', 'note 2', 'note 3']
        expected_message = "Course already added. Notes have been updated."
        self.assertTrue(course_name in student.courses)
        self.assertEqual(expected_notes, student.courses[course_name])
        self.assertEqual(result, expected_message)

    def test_enroll_when_course_does_not_exist_with_notes(self):
        student = Student("Student", {"Python Basics": ['note 1']})
        course_name = "Python Fundamentals"
        result = student.enroll(course_name, ['note 2', 'note 3'], 'Y')
        expected_notes = ['note 2', 'note 3']
        expected_message = "Course and course notes have been added."
        self.assertTrue(course_name in student.courses)
        self.assertEqual(expected_notes, student.courses[course_name])
        self.assertEqual(result, expected_message)

    def test_enroll__when_course_does_not_exist_without_notes(self):
        student = Student("Student", {"Python Basics": ['note 1']})
        course_name = "Python Fundamentals"
        result = student.enroll(course_name, ['note 2', 'note 3'], 'a')

        expected_message = "Course has been added."
        self.assertTrue(course_name in student.courses)
        self.assertEqual([], student.courses[course_name])
        self.assertEqual(result, expected_message)

    def test_add_notes__expect_to_be_correct(self):
        course_name = "Python Basics"
        student = Student("Student", {"Python Basics": ['note 1']})
        result = student.add_notes(course_name, 'note 2')
        expected_message = "Notes have been updated"
        self.assertEqual(['note 1', 'note 2'], student.courses[course_name])
        self.assertEqual(result, expected_message)

    def test_add_notes__expect_to_be_correct_without_notes(self):
        student = Student("Student", {"Python Basics": []})
        course_name = "Python Basics"
        result = student.add_notes(course_name, '')
        expected_message = "Notes have been updated"

        self.assertEqual([''], student.courses[course_name])
        self.assertEqual(result, expected_message)

    def test_add_notes__expect_to_raise(self):
        student = Student("Student", {"Python Basics": ['note 1']})
        with self.assertRaises(Exception) as ex:
            student.add_notes("Python Advanced", ['note 2', 'note 3'])

        expected_message = "Cannot add notes. Course not found."
        self.assertIsNotNone(ex)
        self.assertEqual(expected_message, str(ex.exception))

    def test_leave_course__expect_to_be_correct(self):
        course_name = "Python Basics"
        student = Student("Student", {course_name: ['note 1']})
        result = student.leave_course(course_name)
        expected_message = "Course has been removed"
        self.assertTrue(course_name not in student.courses)
        self.assertEqual(result, expected_message)

    def test_leave_course__expect_to_raise(self):
        student = Student("Student", {"Python Basics": ['note 1']})
        student.enroll('Python Fundamentals', [])
        with self.assertRaises(Exception) as ex:
            student.leave_course("Python Advanced")

        expected_message = "Cannot remove course. Course not found."
        self.assertIsNotNone(ex)
        self.assertEqual(expected_message, str(ex.exception))
