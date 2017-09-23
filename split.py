#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:brief: Module containing implementation of split method.
:author: Michal Modlinski
:created: 02.09.2017
"""
import unittest


def my_split(string, sep=None, maxsplit=-1):

    split_list = []

    if sep is None or sep not in string:
        split_list.append(string)

    elif sep == '':
        raise ValueError

    elif type(sep) != str:
        raise TypeError

    elif sep:
        end = False
        while not end:
            for i in range(len(string) - len(sep) + 1):
                if string[i:i + len(sep)] == sep:
                    first = string[:i]
                    split_list.append(first)
                    string = string[i+len(sep):]
                    break
            else:
                split_list.append(string)
                end = True
    return split_list


# good practise is to add a few test cases before implementing a function
class TestMySplit(unittest.TestCase):

    def test_not_contains_separator(self):
        self.assertEqual(my_split('abc___def___ghi___jkl', 'mno'), ['abc___def___ghi___jkl'])

    def test_contains_part_of_separator(self):
        self.assertEqual(my_split('abc___def___ghi___jkl', '____'), ['abc___def___ghi___jkl'])

    def test_contains_separator(self):
        self.assertEqual(my_split('abc___def___ghi___jkl', '___'), ['abc', 'def', 'ghi', 'jkl'])

    def test_contains_two_separators(self):
        self.assertEqual(my_split('abc___def___ghi___jkl', '__'), ['abc', '_def', '_ghi', '_jkl'])

    def test_contains_three_separators(self):
        self.assertEqual(my_split('abc___def___ghi___jkl', '_'), ['abc', '', '', 'def', '', '', 'ghi', '', '', 'jkl'])

    def test_first_one_letter(self):
        self.assertEqual(my_split('abc___def___cba___fed', 'a'), ['', 'bc___def___cb', '___fed'])

    def test_last_one_letter(self):
        self.assertEqual(my_split('abc___def___cba___fed', 'd'), ['abc___', 'ef___cba___fe', ''])

    def test_no_parameters(self):
        self.assertEqual(my_split('abc___def___ghi___jkl'), ['abc___def___ghi___jkl'])

    def test_separator_longer_than_string(self):
        self.assertEqual(my_split('abc_def', 'longer_than_string'), ['abc_def'])

    def test_value_error_empty_string(self):
        self.assertRaises(ValueError, my_split, 'mic___hal___mod___lin___ski', '')

    def test_type_error_int_one_hundred(self):
        self.assertRaises(TypeError, my_split, 'mic___hal___mod___lin___ski', 100)

    def test_type_error_int_zero(self):
        self.assertRaises(TypeError, my_split, 'mic___hal___mod___lin___ski', 0)

if __name__ == '__main__':
    unittest.main()
