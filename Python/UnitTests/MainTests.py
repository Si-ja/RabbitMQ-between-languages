import unittest
from Brainiac.Brainiac import Brainiac

class TestBrainiacBasicFunctionality(unittest.TestCase):

    def test_square_area_calculations(self):
        # Arrange
        a1 = 4
        area1_excpect = 16

        a2 = 2
        area2_excpect = 4

        a3 = 1.5
        area3_excpect = 2.25

        # Act
        area1_calc = Brainiac.calculate_area_of_square(a1)
        area2_calc = Brainiac.calculate_area_of_square(a2)
        area3_calc = Brainiac.calculate_area_of_square(a3)

        # Assert
        self.assertEqual(area1_excpect, area1_calc)
        self.assertEqual(area2_excpect, area2_calc)
        self.assertEqual(area3_excpect, area3_calc)

    def test_rectangle_area_calculation(self):
        # Arrange
        a1, b1 = 4, 4
        area1_excpect = 16

        a2, b2 = 2.5, 1
        area2_excpect = 2.5

        a3, b3 = 10, 2
        area3_excpect = 20

        # Act
        area1_calc = Brainiac.calculate_area_of_rectangle(a1, b1)
        area2_calc = Brainiac.calculate_area_of_rectangle(a2, b2)
        area3_calc = Brainiac.calculate_area_of_rectangle(a3, b3)

        # Assert
        self.assertEqual(area1_excpect, area1_calc)
        self.assertEqual(area2_excpect, area2_calc)
        self.assertEqual(area3_excpect, area3_calc)

    def test_find_valuesin_in_prime_sequence(self):
        # Arrange
        a1 = 20
        values1_excpect = [2, 3, 5, 7, 11, 13, 17, 19]

        a2 = 50
        values2_excpect = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

        # Act
        values1_calc = Brainiac.find_prime_sequence(a1)
        values2_calc = Brainiac.find_prime_sequence(a2)

        # Assess
        self.assertEqual(values1_excpect, values1_calc)
        self.assertEqual(values2_excpect, values2_calc)
    
class TestIncomingDataParser(unittest.TestCase):
    pass

class TestOutgoingMessagesCreator(unittest.TestCase):
    pass

class TestErrorsHandler(unittest.TestCase):

    def test_Brainiac_calculating_square_errors_handling(self):
        # Arrange
        err_input1 = "foobar"
        err_input2 = -420

        # Act / Assert
        try:
            Brainiac.calculate_area_of_square(err_input1)
        except ValueError as e:
            self.assertEqual(type(e), ValueError)

        try:
            Brainiac.calculate_area_of_square(err_input2)
        except ValueError as e:
            self.assertEqual(type(e), ValueError)

    def test_Brainiac_calculating_rectangle_errors_handling(self):
        # Arrange
        good_input1 = 10
        err_input1 = "foobar"

        good_input2 = 10
        err_input2 = -420

        err_input31 = "food"
        err_input32 = "notfood?"

        # Act / Assert
        try:
            Brainiac.calculate_area_of_rectangle(good_input1, err_input1)
        except ValueError as e:
            self.assertEqual(type(e), ValueError)

        try:
            Brainiac.calculate_area_of_rectangle(good_input2, err_input2)
        except ValueError as e:
            self.assertEqual(type(e), ValueError)

        try:
            Brainiac.calculate_area_of_rectangle(err_input31, err_input32)
        except ValueError as e:
            self.assertEqual(type(e), ValueError)

    def test_Brainiac_calculating_prime_numbers_errors_handling(self):
        # Arrange
        err_input1 = -200000
        err_input2 = "banana"

        # Act / Assert
        try:
            Brainiac.find_prime_sequence(err_input1)
        except ValueError as e:
            self.assertEqual(type(e), ValueError)

        try:
            Brainiac.find_prime_sequence(err_input2)
        except ValueError as e:
            self.assertEqual(type(e), ValueError)


if __name__ == "__main__":
    unittest.main()
