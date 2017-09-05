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

    if sep == '':
        raise ValueError

    elif not sep or sep not in string:
        split_list.append(string)

    elif type(sep) != str:
        raise TypeError

    elif sep:
        el = ''
        ind = 0
        loop_range = len(string)
        while ind < loop_range:
            if string[ind:ind + len(sep)] != sep:
                el += string[ind]
                ind += 1
            if (string[ind:ind + len(sep)] == sep) or (ind == loop_range):
                split_list.append(el)
                el = ''
                ind += len(sep)

    return split_list


class TestMySplit(unittest.TestCase):

    # class variable using self like sleep
    attribute = 'new'
    string_1 = 'mic___hal___mod___lin___ski'
    sep_1 = '___'
    sep_2 = '__'
    sep_3 = '_'
    sep_4 = 'mic'
    sep_5 = 'ski'
    sep_6 = 'm'
    sep_7 = 'i'
    sep_8 = 'l_'
    sep_9 = '_m'
    sep_10 = ''
    sep_11 = 'long---------------------------------string'
    sep_12 = 100
    sep_13 = 0  # important test case for this

    # def __init__(self, methodName='runTest'):
    #     super().__init__(methodName=methodName)
    #
    #     self.attribute = 'new'
    #     self.string_1 = 'mic___hal___mod___lin___ski'
    #     self.sep_1 = '___'
    #     self.sep_2 = '__'
    #     self.sep_3 = '_'
    #     self.sep_4 = 'mic'
    #     self.sep_5 = 'ski'
    #     self.sep_6 = 'm'
    #     self.sep_7 = 'i'
    #     self.sep_8 = 'l_'
    #     self.sep_9 = '_m'
    #     self.sep_10 = ''
    #     self.sep_11 = 'long---------------------------------string'
    #     self.sep_12 = 100
    #     self.sep_13 = 0  # important test case for this

    def test_1(self):
        self.assertEqual(my_split(self.string_1, self.sep_1), self.string_1.split(self.sep_1))

    def test_2(self):
        self.assertEqual(my_split(self.string_1, self.sep_2), self.string_1.split(self.sep_2))

    def test_3(self):
        self.assertEqual(my_split(self.string_1, self.sep_3), self.string_1.split(self.sep_3))

    def test_4(self):
        self.assertEqual(my_split(self.string_1, self.sep_4), self.string_1.split(self.sep_4))

    # def test_5(self):
    #     self.assertEqual(my_split(self.string_1, self.sep_5), self.string_1.split(self.sep_5))

    def test_6(self):
        self.assertEqual(my_split(self.string_1, self.sep_6), self.string_1.split(self.sep_6))

    # def test_7(self):
    #     self.assertEqual(my_split(self.string_7, self.sep_7), self.string_7.split(self.sep_7))

    def test_8(self):
        self.assertEqual(my_split(self.string_1, self.sep_8), self.string_1.split(self.sep_8))

    def test_9(self):
        self.assertEqual(my_split(self.string_1, self.sep_9), self.string_1.split(self.sep_9))

    # def test_10(self):
        # self.assertRaises(ValueError, my_split(self.string_1, self.sep_10))

    def test_11(self):
        self.assertEqual(my_split(self.string_1), self.string_1.split())

    def test_12(self):
        self.assertEqual(my_split(self.string_1, self.sep_11), self.string_1.split(self.sep_11))

    # def test_13(self):
        # self.assertRaises(TypeError, my_split(self.string_1, self.sep_12))

if __name__ == '__main__':
    unittest.main()
