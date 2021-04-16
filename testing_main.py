import unittest
from funTimes import *


class BMITest(unittest.TestCase):
    def test_bmi_calc_normal(self):
        real = bmi_calc(5, 3, 125)
        assumed = ['Normal Weight', 22.7]
        self.assertEqual(assumed, real)

    def test_bmi_calc_obese(self):
        real = bmi_calc(6, 3, 300)
        assumed = ['Obese', 38.4]
        self.assertEqual(assumed, real)

    def test_bmi_calc_underweight(self):
        real = bmi_calc(6, 3, 120)
        assumed = ['Underweight', 15.4]
        self.assertEqual(assumed, real)

    def test_bmi_calc_overweight(self):
        real = bmi_calc(6, 3, 220)
        assumed = ['Overweight', 28.2]
        self.assertEqual(assumed, real)

    def test_pound_to_kg(self):
        kg = pound_to_kg(1)
        self.assertEqual(kg, 0.45)

    def test_height_to_inches(self):
        inches = height_to_inches(1, 1)
        self.assertEqual(inches, 13)

    def test_inches_to_meters(self):
        meters = inches_to_meters(1)
        self.assertEqual(meters, 0.025)


class RetirementTest(unittest.TestCase):
    def test_retirement_calc(self):
        retire_age = retirement_calc(21, 40000, 0.25, 500000)
        self.assertAlmostEqual(retire_age, 58.00, 1)

    def test_saved_per_year(self):
        saved = saved_per_year(40000, .25)
        self.assertEqual(saved, 13500)

    def test_years_to_goal(self):
        years = years_to_goal(100000, 1000000)
        self.assertEqual(years, 10)


class InterfaceTest(unittest.TestCase):
    def test_check_init_input(self):
        real = check_init_input('1')
        self.assertEqual(real, True)

    def test_bad_init_input(self):
        real = check_init_input('one')
        self.assertEqual(real, False)

    def test_handle_bmi_input(self):
        real = handle_bmi_input('5 3 125')
        assumed = ['Normal Weight', 22.7]
        self.assertEqual(assumed, real)

    def test_string_bmi_input(self):
        with self.assertRaises(ValueError) as real:
            handle_bmi_input('five 3 125')
        self.assertEqual(real.exception.__class__, ValueError)

    def test_indexerr_bmi_input(self):
        with self.assertRaises(IndexError) as real:
            handle_bmi_input('5')
        self.assertEqual(real.exception.__class__, IndexError)

    def test_float_bmi_input(self):
        with self.assertRaises(ValueError) as real:
            handle_bmi_input('5.4 3 125')
        self.assertEqual(real.exception.__class__, ValueError)

    def test_handle_retirement_input(self):
        real = handle_retirement_input('21 40000 0.25 500000')
        assumed = 58.0
        self.assertAlmostEqual(assumed, real, 1)

    def test_string_retirement_input(self):
        with self.assertRaises(ValueError) as real:
            handle_retirement_input('twenty-one 40000 0.25 500000')
        self.assertEqual(real.exception.__class__, ValueError)

    def test_indexerr_retirement_input(self):
        with self.assertRaises(IndexError) as real:
            handle_retirement_input('21')
        self.assertEqual(real.exception.__class__, IndexError)

    def test_over_prc_retirement(self):
        with self.assertRaises(ValueError) as real:
            handle_retirement_input('21 40000 1.1 50000')
        self.assertEqual(real.exception.__class__, ValueError)

