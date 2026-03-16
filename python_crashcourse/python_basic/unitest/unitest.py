import unittest

from name_function import get_formatted_name
from survey import AnoymousSurvey
from employee import Employee
class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('Ousmane', 'Diallo')
        self.assertEqual(formatted_name, 'Ousmane Diallo')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name("Fnu", "Diallo", "Anchita")
        self.assertEqual(formatted_name, 'Fnu Anchita Diallo')


class AnoymousSurveys(unittest.TestCase):
    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnoymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

class EmployeeTestCase(unittest.TestCase):
    def test_give_default_raise(self):
        employee = Employee(first_name='Ousmane', last_name='Diallo')
        self.assertEqual(employee.salary, 5000)



unittest.main()