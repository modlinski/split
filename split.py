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

    if type(sep) != str and sep is not None or type(maxsplit) != int:
        raise TypeError
    elif sep == '':
        raise ValueError
    elif sep is None or sep not in string or maxsplit == 0:
        split_list.append(string)
    elif sep:
        if maxsplit <= -1:
            end = False
            while not end:
                for i in range(len(string) - len(sep) + 1):
                    if string[i:i + len(sep)] == sep:
                        split_list.append(string[:i])
                        string = string[i+len(sep):]
                        break
                else:
                    split_list.append(string)
                    end = True
        else:
            end = False
            while not end and maxsplit > 0:
                for i in range(len(string) - len(sep) + 1):
                    if string[i:i + len(sep)] == sep:
                        split_list.append(string[:i])
                        string = string[i+len(sep):]
                        maxsplit -= 1
                        if maxsplit == 0:
                            split_list.append(string)
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

    def test_string_the_same_as_parameter(self):
        self.assertEqual(my_split('abc___def___ghi', 'abc___def___ghi'), ['', ''])

    def test_no_parameters(self):
        self.assertEqual(my_split('abc___def___ghi___jkl'), ['abc___def___ghi___jkl'])

    def test_separator_longer_than_string(self):
        self.assertEqual(my_split('abc_def', 'longer_than_string'), ['abc_def'])

    def test_type_error_maxsplit_stopped_by_maxsplit(self):
        self.assertEqual(my_split('abc___def___ghi___jkl', '___', 2), ['abc', 'def', 'ghi___jkl'])

    def test_type_error_maxsplit_stopped_by_end_parameter(self):
        self.assertEqual(my_split('abc___def___ghi___jkl', '___', 20), ['abc', 'def', 'ghi', 'jkl'])

    def test_value_error_sep_empty_string(self):
        self.assertRaises(ValueError, my_split, 'abc___def___ghi___jkl', '')

    def test_type_error_sep_int_one_hundred(self):
        self.assertRaises(TypeError, my_split, 'abc___def___ghi___jkl', 100)

    def test_type_error_sep_int_zero(self):
        self.assertRaises(TypeError, my_split, 'abc___def___ghi___jkl', 0)

    def test_type_error_sep_empty_list(self):
        self.assertRaises(TypeError, my_split, 'abc___def___ghi___jkl', [])

    def test_type_error_maxsplit_float(self):
        self.assertRaises(TypeError, my_split, 'abc___def___ghi___jkl', 'a', -1.5)

if __name__ == '__main__':
    unittest.main()
