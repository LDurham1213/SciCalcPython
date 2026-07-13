import math
import unittest

from sciCalc import SciCalc


class TestSciCalc(unittest.TestCase):

    def setUp(self):
        """
        Create a new scientific calculator before every test.

        This ensures that every test is independent.
        """
        self.calc = SciCalc()

    # ============================================================
    # Factorial tests
    # ============================================================

    def test_factorial_of_positive_whole_number(self):
        self.calc.setDisplay(5)

        result = self.calc.factorial()

        self.assertEqual(result, 120)
        self.assertEqual(self.calc.getDisplay(), 120)

    def test_factorial_of_zero_is_one(self):
        self.calc.setDisplay(0)

        result = self.calc.factorial()

        self.assertEqual(result, 1)

    def test_factorial_of_one_is_one(self):
        self.calc.setDisplay(1)

        result = self.calc.factorial()

        self.assertEqual(result, 1)

    def test_factorial_rejects_negative_number(self):
        self.calc.setDisplay(-5)

        result = self.calc.factorial()

        self.assertEqual(
            result,
            "Factorial requires a non-negative number"
        )
        self.assertTrue(self.calc.hasError())

    def test_factorial_rejects_decimal_number(self):
        self.calc.setDisplay(4.5)

        result = self.calc.factorial()

        self.assertEqual(
            result,
            "Factorial requries a whole number"
        )
        self.assertTrue(self.calc.hasError())

    def test_factorial_is_blocked_when_error_exists(self):
        self.calc.setDisplay("invalid")

        result = self.calc.factorial()

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)

    # ============================================================
    # Base-10 logarithm tests
    # ============================================================

    def test_log_of_one_is_zero(self):
        self.calc.setDisplay(1)

        result = self.calc.log()

        self.assertEqual(result, 0)

    def test_log_of_one_hundred_is_two(self):
        self.calc.setDisplay(100)

        result = self.calc.log()

        self.assertEqual(result, 2)

    def test_log_of_one_thousand_is_three(self):
        self.calc.setDisplay(1000)

        result = self.calc.log()

        self.assertEqual(result, 3)

    def test_log_of_zero_sets_error(self):
        self.calc.setDisplay(0)

        result = self.calc.log()

        self.assertEqual(
            result,
            "Log undefined for zeror or negative numbers"
        )
        self.assertTrue(self.calc.hasError())

    def test_log_of_negative_number_sets_error(self):
        self.calc.setDisplay(-10)

        result = self.calc.log()

        self.assertEqual(
            result,
            "Log undefined for zeror or negative numbers"
        )
        self.assertTrue(self.calc.hasError())

    # ============================================================
    # Inverse-logarithm tests
    # ============================================================

    def test_inverse_log_of_two_is_one_hundred(self):
        self.calc.setDisplay(2)

        result = self.calc.inverse_log()

        self.assertEqual(result, 100)

    def test_inverse_log_of_zero_is_one(self):
        self.calc.setDisplay(0)

        result = self.calc.inverse_log()

        self.assertEqual(result, 1)


    # ============================================================
    # Natural-logarithm tests
    # ============================================================


    def test_natural_log_of_one_is_zero(self):
        self.calc.setDisplay(1)

        result = self.calc.natural_log()

        self.assertEqual(result, 0)

    def test_natural_log_of_zero_sets_error(self):
        self.calc.setDisplay(0)

        result = self.calc.natural_log()

        self.assertEqual(
            result,
            "Natural log undefined for zero or negative nubmers"
        )
        self.assertTrue(self.calc.hasError())

    def test_natural_log_of_negative_number_sets_error(self):
        self.calc.setDisplay(-5)

        result = self.calc.natural_log()

        self.assertEqual(
            result,
            "Natural log undefined for zero or negative nubmers"
        )
        self.assertTrue(self.calc.hasError())

    # ============================================================
    # Inverse-natural-logarithm tests
    # ============================================================

    def test_inverse_natural_log_of_zero_is_one(self):
        self.calc.setDisplay(0)

        result = self.calc.inverse_natural_log()

        self.assertEqual(result, 1)

    # ============================================================
    # Tip-calculator tests
    # ============================================================

    def test_tip_calculator_adds_twenty_percent_tip(self):
        result = self.calc.tip_calculator(100, 20)

        self.assertEqual(result, 120)
        self.assertEqual(self.calc.getDisplay(), 120)


    def test_tip_calculator_allows_zero_tip(self):
        result = self.calc.tip_calculator(75, 0)

        self.assertEqual(result, 75)

    def test_tip_calculator_rejects_negative_bill(self):
        result = self.calc.tip_calculator(-100, 20)

        self.assertEqual(result, "Amounts cannot be negative")
        self.assertTrue(self.calc.hasError())

    def test_tip_calculator_rejects_negative_tip(self):
        result = self.calc.tip_calculator(100, -20)

        self.assertEqual(result, "Amounts cannot be negative")
        self.assertTrue(self.calc.hasError())

    def test_tip_calculator_rejects_invalid_bill(self):
        result = self.calc.tip_calculator("100", 20)

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)

    def test_tip_calculator_rejects_invalid_tip(self):
        result = self.calc.tip_calculator(100, "20")

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)

    # ============================================================
    # Temperature-converter tests
    # ============================================================


    def test_temperature_converter_rejects_invalid_temperature(self):
        result = self.calc.temperature_converter("hot", "C")

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)

    def test_temperature_converter_rejects_invalid_conversion(self):
        result = self.calc.temperature_converter(100, "X")

        self.assertEqual(result, "Use C or F")
        self.assertTrue(self.calc.hasError())

    # ============================================================
    # Trigonometric-mode tests
    # ============================================================

    def test_default_trig_mode_is_radians(self):
        self.assertEqual(self.calc.getTrigMode(), "Radians")

    def test_switch_units_mode_sets_degrees(self):
        result = self.calc.switchUnitsMode("Degrees")

        self.assertEqual(result, "Degrees")
        self.assertEqual(self.calc.getTrigMode(), "Degrees")

    def test_switch_units_mode_sets_radians(self):
        self.calc.switchUnitsMode("Degrees")

        result = self.calc.switchUnitsMode("Radians")

        self.assertEqual(result, "Radians")

    def test_switch_units_mode_rotates_from_radians_to_degrees(self):
        result = self.calc.switchUnitsMode()

        self.assertEqual(result, "Degrees")

    def test_switch_units_mode_rotates_from_degrees_to_radians(self):
        self.calc.switchUnitsMode("Degrees")

        result = self.calc.switchUnitsMode()

        self.assertEqual(result, "Radians")

    # ============================================================
    # Sine tests
    # ============================================================

    def test_sine_of_zero_radians_is_zero(self):
        self.calc.setDisplay(0)

        result = self.calc.sine()

        self.assertEqual(result, 0.0)

    def test_sine_of_pi_over_two_radians_is_one(self):
        self.calc.setDisplay(math.pi / 2)

        result = self.calc.sine()

        self.assertAlmostEqual(result, 1.0, places=7)

    def test_sine_of_ninety_degrees_is_one(self):
        self.calc.switchUnitsMode("Degrees")
        self.calc.setDisplay(90)

        result = self.calc.sine()

        self.assertAlmostEqual(result, 1.0, places=7)

    # ============================================================
    # Cosine tests
    # ============================================================

    def test_cosine_of_zero_radians_is_one(self):
        self.calc.setDisplay(0)

        result = self.calc.cosine()

        self.assertAlmostEqual(result, 1.0, places=7)

    def test_cosine_of_pi_radians_is_negative_one(self):
        self.calc.setDisplay(math.pi)

        result = self.calc.cosine()

        self.assertAlmostEqual(result, -1.0, places=7)

    def test_cosine_of_sixty_degrees_is_point_five(self):
        self.calc.switchUnitsMode("Degrees")
        self.calc.setDisplay(60)

        result = self.calc.cosine()

        self.assertAlmostEqual(result, 0.5, places=7)

    def test_cosine_of_ninety_degrees_is_zero(self):
        self.calc.switchUnitsMode("Degrees")
        self.calc.setDisplay(90)

        result = self.calc.cosine()

        self.assertEqual(result, 0.0)

    # ============================================================
    # Tangent tests
    # ============================================================

    def test_tangent_of_zero_radians_is_zero(self):
        self.calc.setDisplay(0)

        result = self.calc.tangent()

        self.assertEqual(result, 0.0)

    def test_tangent_of_pi_over_four_radians_is_one(self):
        self.calc.setDisplay(math.pi / 4)

        result = self.calc.tangent()

        self.assertAlmostEqual(result, 1.0, places=7)

    def test_tangent_of_forty_five_degrees_is_one(self):
        self.calc.switchUnitsMode("Degrees")
        self.calc.setDisplay(45)

        result = self.calc.tangent()

        self.assertAlmostEqual(result, 1.0, places=7)

    # ============================================================
    # Inverse-sine tests
    # ============================================================

    def test_inverse_sine_of_one_in_radians(self):
        self.calc.setDisplay(1)

        result = self.calc.inverse_sine()

        self.assertAlmostEqual(result, math.pi / 2, places=7)

    def test_inverse_sine_of_one_in_degrees(self):
        self.calc.switchUnitsMode("Degrees")
        self.calc.setDisplay(1)

        result = self.calc.inverse_sine()

        self.assertAlmostEqual(result, 90.0, places=7)

    def test_inverse_sine_of_zero_is_zero(self):
        self.calc.setDisplay(0)

        result = self.calc.inverse_sine()

        self.assertEqual(result, 0.0)

    # ============================================================
    # Inverse-cosine tests
    # ============================================================

    def test_inverse_cosine_of_one_in_radians(self):
        self.calc.setDisplay(1)

        result = self.calc.inverse_cosine()

        self.assertEqual(result, 0.0)

    def test_inverse_cosine_of_zero_in_degrees(self):
        self.calc.switchUnitsMode("Degrees")
        self.calc.setDisplay(0)

        result = self.calc.inverse_cosine()

        self.assertAlmostEqual(result, 90.0, places=7)

    # ============================================================
    # Inverse-tangent tests
    # ============================================================

    def test_inverse_tangent_of_one_in_radians(self):
        self.calc.setDisplay(1)

        result = self.calc.inverse_tangent()

        self.assertAlmostEqual(result, math.pi / 4, places=7)

    def test_inverse_tangent_of_one_in_degrees(self):
        self.calc.switchUnitsMode("Degrees")
        self.calc.setDisplay(1)

        result = self.calc.inverse_tangent()

        self.assertAlmostEqual(result, 45.0, places=7)

    def test_inverse_tangent_of_zero_is_zero(self):
        self.calc.setDisplay(0)

        result = self.calc.inverse_tangent()

        self.assertEqual(result, 0.0)

    # ============================================================
    # Inherited-error-state tests
    # ============================================================

    def test_scientific_operation_is_blocked_during_error(self):
        self.calc.setDisplay("invalid")

        result = self.calc.factorial()

        self.assertEqual(result, self.calc.INVALID_INPUT_ERROR)

    def test_clear_allows_scientific_operation_after_error(self):
        self.calc.setDisplay("invalid")
        self.calc.clear()
        self.calc.setDisplay(5)

        result = self.calc.factorial()

        self.assertEqual(result, 120)
        self.assertFalse(self.calc.hasError())


if __name__ == "__main__":
    unittest.main()