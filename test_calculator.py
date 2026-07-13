import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """
        Create a new Calculator before every test.

        This keeps each test independent.
        """
        self.calc = Calculator()

    # -------------------------------------------------
    # Initial state and display tests
    # -------------------------------------------------

    def test_default_display_is_zero(self):
        self.assertEqual(self.calc.getDisplay(), 0)

    def test_default_error_is_none(self):
        self.assertFalse(self.calc.hasError())

    def test_default_memory_is_zero(self):
        self.assertEqual(self.calc.memory, 0)

    def test_default_trig_mode_is_radians(self):
        self.assertEqual(self.calc.trig_mode, "Radians")

    def test_set_display_updates_display(self):
        result = self.calc.setDisplay(25)

        self.assertEqual(result, 25)
        self.assertEqual(self.calc.getDisplay(), 25)

    def test_set_display_accepts_decimal_number(self):
        result = self.calc.setDisplay(12.5)

        self.assertEqual(result, 12.5)

    def test_set_display_rejects_string(self):
        result = self.calc.setDisplay("hello")

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)
        self.assertTrue(self.calc.hasError())

    def test_set_display_rejects_boolean(self):
        result = self.calc.setDisplay(True)

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)
        self.assertTrue(self.calc.hasError())

    def test_set_display_is_blocked_when_error_exists(self):
        self.calc.setDisplay("bad value")

        result = self.calc.setDisplay(10)

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)
        self.assertTrue(self.calc.hasError())

    def test_clear_resets_display_and_error(self):
        self.calc.setDisplay("bad value")

        result = self.calc.clear()

        self.assertEqual(result, 0)
        self.assertEqual(self.calc.getDisplay(), 0)
        self.assertFalse(self.calc.hasError())

    # -------------------------------------------------
    # Number validation tests
    # -------------------------------------------------

    def test_is_valid_number_accepts_integer(self):
        self.assertTrue(self.calc.isValidNumber(10))

    def test_is_valid_number_accepts_float(self):
        self.assertTrue(self.calc.isValidNumber(10.5))

    def test_is_valid_number_rejects_string(self):
        self.assertFalse(self.calc.isValidNumber("10"))

    def test_is_valid_number_rejects_boolean(self):
        self.assertFalse(self.calc.isValidNumber(True))

    # -------------------------------------------------
    # Memory tests
    # -------------------------------------------------

    def test_memory_add_adds_display_to_memory(self):
        self.calc.setDisplay(10)

        result = self.calc.memory_add()

        self.assertEqual(result, 10)
        self.assertEqual(self.calc.memory, 10)
        self.assertEqual(self.calc.getDisplay(), 10)

    def test_memory_add_accumulates_values(self):
        self.calc.setDisplay(10)
        self.calc.memory_add()

        self.calc.setDisplay(5)
        result = self.calc.memory_add()

        self.assertEqual(result, 15)
        self.assertEqual(self.calc.memory, 15)
        self.assertEqual(self.calc.getDisplay(), 15)

    def test_memory_clear_resets_memory_to_zero(self):
        self.calc.setDisplay(10)
        self.calc.memory_add()

        result = self.calc.memory_clear()

        self.assertEqual(self.calc.memory, 0)
        self.assertEqual(result, 10)

    def test_memory_recall_copies_memory_to_display(self):
        self.calc.setDisplay(12)
        self.calc.memory_store()

        self.calc.setDisplay(0)
        result = self.calc.memory_recall()

        self.assertEqual(result, 12)
        self.assertEqual(self.calc.getDisplay(), 12)

    def test_memory_store_saves_current_display(self):
        self.calc.setDisplay(22)

        result = self.calc.memory_store()

        self.assertEqual(result, 22)
        self.assertEqual(self.calc.memory, 22)

    def test_memory_operation_is_blocked_when_error_exists(self):
        self.calc.setDisplay("bad value")

        result = self.calc.memory_add()

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)

    # -------------------------------------------------
    # Addition tests
    # -------------------------------------------------

    def test_add_two_positive_numbers(self):
        result = self.calc.add(5, 3)

        self.assertEqual(result, 8)
        self.assertEqual(self.calc.getDisplay(), 8)

    def test_add_positive_and_negative_numbers(self):
        result = self.calc.add(10, -4)

        self.assertEqual(result, 6)

    def test_add_rejects_invalid_first_number(self):
        result = self.calc.add("5", 3)

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)
        self.assertTrue(self.calc.hasError())

    def test_add_rejects_invalid_second_number(self):
        result = self.calc.add(5, "3")

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)

    # -------------------------------------------------
    # Subtraction tests
    # -------------------------------------------------

    def test_subtract_two_numbers(self):
        result = self.calc.subtract(10, 4)

        self.assertEqual(result, 6)
        self.assertEqual(self.calc.getDisplay(), 6)

    def test_subtract_can_return_negative_result(self):
        result = self.calc.subtract(4, 10)

        self.assertEqual(result, -6)

    def test_subtract_rejects_invalid_input(self):
        result = self.calc.subtract(10, "4")

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)

    # -------------------------------------------------
    # Multiplication tests
    # -------------------------------------------------

    def test_multiply_two_numbers(self):
        result = self.calc.multiply(6, 7)

        self.assertEqual(result, 42)
        self.assertEqual(self.calc.getDisplay(), 42)

    def test_multiply_by_zero(self):
        result = self.calc.multiply(9, 0)

        self.assertEqual(result, 0)

    def test_multiply_rejects_invalid_input(self):
        result = self.calc.multiply("6", 7)

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)

    # -------------------------------------------------
    # Division tests
    # -------------------------------------------------

    def test_divide_two_numbers(self):
        result = self.calc.divide(20, 4)

        self.assertEqual(result, 5)
        self.assertEqual(self.calc.getDisplay(), 5)

    def test_divide_returns_decimal_result(self):
        result = self.calc.divide(5, 2)

        self.assertEqual(result, 2.5)

    def test_divide_by_zero_sets_error(self):
        result = self.calc.divide(10, 0)

        self.assertEqual(result, self.calc.DIVIDE_BY_ZERO_ERROR)
        self.assertTrue(self.calc.hasError())

    def test_divide_rejects_invalid_input(self):
        result = self.calc.divide(10, "2")

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)

    # -------------------------------------------------
    # Error-state tests
    # -------------------------------------------------

    def test_operation_is_blocked_when_error_exists(self):
        self.calc.divide(10, 0)

        result = self.calc.add(2, 3)

        self.assertEqual(result, self.calc.DIVIDE_BY_ZERO_ERROR)
        self.assertTrue(self.calc.hasError())

    def test_clear_allows_operation_after_error(self):
        self.calc.divide(10, 0)
        self.calc.clear()

        result = self.calc.add(2, 3)

        self.assertEqual(result, 5)
        self.assertFalse(self.calc.hasError())

    # -------------------------------------------------
    # Inverse tests
    # -------------------------------------------------

    def test_inverse_of_positive_number(self):
        self.calc.setDisplay(4)

        result = self.calc.inverse()

        self.assertEqual(result, 0.25)

    def test_inverse_of_negative_number(self):
        self.calc.setDisplay(-4)

        result = self.calc.inverse()

        self.assertEqual(result, -0.25)

    def test_inverse_of_zero_sets_error(self):
        self.calc.setDisplay(0)

        result = self.calc.inverse()

        self.assertEqual(result, self.calc.DIVIDE_BY_ZERO_ERROR)
        self.assertTrue(self.calc.hasError())

    # -------------------------------------------------
    # Exponentiation tests
    # -------------------------------------------------

    def test_exponentiate_positive_integer_exponent(self):
        self.calc.setDisplay(2)

        result = self.calc.exponentiate(3)

        self.assertEqual(result, 8)

    def test_exponentiate_zero_exponent(self):
        self.calc.setDisplay(5)

        result = self.calc.exponentiate(0)

        self.assertEqual(result, 1)

    def test_exponentiate_negative_exponent(self):
        self.calc.setDisplay(2)

        result = self.calc.exponentiate(-2)

        self.assertEqual(result, 0.25)

    def test_exponentiate_rejects_invalid_exponent(self):
        self.calc.setDisplay(2)

        result = self.calc.exponentiate("3")

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)

    def test_exponentiate_negative_base_fractional_power_sets_error(self):
        self.calc.setDisplay(-4)

        result = self.calc.exponentiate(0.5)

        self.assertEqual(result, self.calc.INVALID_EXPONENT_ERROR)
        self.assertTrue(self.calc.hasError())

    def test_zero_to_negative_exponent_sets_divide_by_zero_error(self):
        self.calc.setDisplay(0)

        result = self.calc.exponentiate(-1)

        self.assertEqual(result, self.calc.DIVIDE_BY_ZERO_ERROR)

    # -------------------------------------------------
    # Switch-sign tests
    # -------------------------------------------------

    def test_switch_sign_changes_positive_to_negative(self):
        self.calc.setDisplay(10)

        result = self.calc.switch_sign()

        self.assertEqual(result, -10)

    def test_switch_sign_changes_negative_to_positive(self):
        self.calc.setDisplay(-10)

        result = self.calc.switch_sign()

        self.assertEqual(result, 10)

    def test_switch_sign_of_zero_remains_zero(self):
        self.calc.setDisplay(0)

        result = self.calc.switch_sign()

        self.assertEqual(result, 0)

    # -------------------------------------------------
    # Square tests
    # -------------------------------------------------

    def test_square_positive_number(self):
        result = self.calc.square(5)

        self.assertEqual(result, 25)
        self.assertEqual(self.calc.getDisplay(), 25)

    def test_square_negative_number(self):
        result = self.calc.square(-4)

        self.assertEqual(result, 16)

    def test_square_rejects_invalid_input(self):
        result = self.calc.square("5")

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)

    # -------------------------------------------------
    # Square-root tests
    # -------------------------------------------------

    def test_square_root_of_perfect_square(self):
        result = self.calc.squareroot(81)

        self.assertEqual(result, 9)
        self.assertEqual(self.calc.getDisplay(), 9)

    def test_square_root_of_zero(self):
        result = self.calc.squareroot(0)

        self.assertEqual(result, 0)

    def test_square_root_of_decimal(self):
        result = self.calc.squareroot(2.25)

        self.assertEqual(result, 1.5)

    def test_square_root_of_negative_number_sets_error(self):
        result = self.calc.squareroot(-9)

        self.assertEqual(
            result,
            "Cannot calculate the square root of a negative number"
        )
        self.assertTrue(self.calc.hasError())

    def test_square_root_rejects_invalid_input(self):
        result = self.calc.squareroot("81")

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)

    # -------------------------------------------------
    # Absolute-value tests
    # -------------------------------------------------

    def test_absolute_value_changes_negative_to_positive(self):
        self.calc.setDisplay(-15)

        result = self.calc.absolute_value()

        self.assertEqual(result, 15)

    def test_absolute_value_keeps_positive_number_positive(self):
        self.calc.setDisplay(15)

        result = self.calc.absolute_value()

        self.assertEqual(result, 15)

    def test_absolute_value_of_zero_is_zero(self):
        self.calc.setDisplay(0)

        result = self.calc.absolute_value()

        self.assertEqual(result, 0)

    # -------------------------------------------------
    # Percentage tests
    # -------------------------------------------------

    def test_percentage_divides_positive_number_by_one_hundred(self):
        self.calc.setDisplay(25)

        result = self.calc.percentage()

        self.assertEqual(result, 0.25)

    def test_percentage_divides_negative_number_by_one_hundred(self):
        self.calc.setDisplay(-25)

        result = self.calc.percentage()

        self.assertEqual(result, -0.25)

    def test_percentage_of_zero_is_zero(self):
        self.calc.setDisplay(0)

        result = self.calc.percentage()

        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()