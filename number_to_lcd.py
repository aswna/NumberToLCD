#!/usr/bin/env python
# encoding: utf-8

"""Convert given decimal number to a (unlimited length) seven-segments display.

The seven-segments display, with all segments switched on is the following:
  ' _ '
  '|_|'
  '|_|'
"""

LCD_DIGITS = {0: [(' _ '),
                  ('| |'),
                  ('|_|')],
              1: [('   '),
                  ('  |'),
                  ('  |')],
              2: [(' _ '),
                  (' _|'),
                  ('|_ ')],
              3: [(' _ '),
                  (' _|'),
                  (' _|')],
              4: [('   '),
                  ('|_|'),
                  ('  |')],
              5: [(' _ '),
                  ('|_ '),
                  (' _|')],
              6: [(' _ '),
                  ('|_ '),
                  ('|_|')],
              7: [(' _ '),
                  ('| |'),
                  ('  |')],
              8: [(' _ '),
                  ('|_|'),
                  ('|_|')],
              9: [(' _ '),
                  ('|_|'),
                  (' _|')]}


class LCD(object):
    @classmethod
    def display(cls, number):
        for lcd_row in cls._convert_number(number):
            print(lcd_row)

    @classmethod
    def _convert_number(cls, number):
        lcd_rows = ['', '', '']
        for char in str(number):
            digit = int(char)
            for index, lcd_row in enumerate(cls._convert_digit(digit)):
                lcd_rows[index] = '{0}{1}'.format(lcd_rows[index], lcd_row)
        return lcd_rows

    @classmethod
    def _convert_digit(cls, digit):
        return LCD_DIGITS[digit]


def show_example():
    digits = '1234567890'
    for i in range(1, 11):
        LCD.display(digits[:i])

if __name__ == '__main__':
    show_example()
