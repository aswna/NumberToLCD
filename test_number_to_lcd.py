#!/usr/bin/env python
# encoding: utf-8

"""Test the conversion of given decimal number to seven-segments display."""

import cStringIO
import sys
import unittest

from number_to_lcd import LCD


ZERO = (' _ \n'
        '| |\n'
        '|_|\n')

ONE = ('   \n'
       '  |\n'
       '  |\n')

TWO = (' _ \n'
       ' _|\n'
       '|_ \n')

THREE = (' _ \n'
         ' _|\n'
         ' _|\n')

FOUR = ('   \n'
        '|_|\n'
        '  |\n')

FIVE = (' _ \n'
        '|_ \n'
        ' _|\n')

SIX = (' _ \n'
       '|_ \n'
       '|_|\n')

SEVEN = (' _ \n'
         '| |\n'
         '  |\n')

EIGHT = (' _ \n'
         '|_|\n'
         '|_|\n')

NINE = (' _ \n'
        '|_|\n'
        ' _|\n')

TEN = ('    _ \n'
       '  || |\n'
       '  ||_|\n')

EIGHTY_EIGHT = (' _  _ \n'
                '|_||_|\n'
                '|_||_|\n')

ONEHUNDRED_TWENTY_THREE = ('    _  _ \n'
                           '  | _| _|\n'
                           '  ||_  _|\n')


class RedirectStdOut(object):
    def __init__(self, stdout=None):
        self._stdout = stdout or sys.stdout
        self.old_stdout = None

    def __enter__(self):
        self.old_stdout = sys.stdout
        self.old_stdout.flush()
        sys.stdout = self._stdout

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush()
        sys.stdout = self.old_stdout


class TestLCD(unittest.TestCase):
    def test_number_zero_printed(self):
        self._assert_lcd_display(0, ZERO)

    def test_number_one_printed(self):
        self._assert_lcd_display(1, ONE)

    def test_number_two_printed(self):
        self._assert_lcd_display(2, TWO)

    def test_number_three_printed(self):
        self._assert_lcd_display(3, THREE)

    def test_number_four_printed(self):
        self._assert_lcd_display(4, FOUR)

    def test_number_five_printed(self):
        self._assert_lcd_display(5, FIVE)

    def test_number_six_printed(self):
        self._assert_lcd_display(6, SIX)

    def test_number_seven_printed(self):
        self._assert_lcd_display(7, SEVEN)

    def test_number_eight_printed(self):
        self._assert_lcd_display(8, EIGHT)

    def test_number_nine_printed(self):
        self._assert_lcd_display(9, NINE)

    def test_number_ten_printed(self):
        self._assert_lcd_display(10, TEN)

    def test_number_eighty_eight_printed(self):
        self._assert_lcd_display(88, EIGHTY_EIGHT)

    def test_number_onehundred_twenty_three_printed(self):
        self._assert_lcd_display(123, ONEHUNDRED_TWENTY_THREE)

    def _assert_lcd_display(self, number, expected_printout):
        my_stdout = cStringIO.StringIO()
        with RedirectStdOut(stdout=my_stdout):
            LCD.display(number)
            self._assert_multiline_strings_equal(expected_printout,
                                                 my_stdout.getvalue())

    def _assert_multiline_strings_equal(self, expected_string, real_string):
        return self.assertEqual(self._get_line_list(expected_string),
                                self._get_line_list(real_string))

    @classmethod
    def _get_line_list(cls, string_with_line_breaks):
        return string_with_line_breaks.split('\n')


def run_unit_tests():
    lcd = unittest.TestLoader().loadTestsFromTestCase(TestLCD)
    all_suites = unittest.TestSuite([lcd])
    unittest.TextTestRunner(verbosity=2).run(all_suites)


if __name__ == '__main__':
    run_unit_tests()
