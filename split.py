#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:brief: Module containing implementation of split method.
:author: Michal Modlinski
:created: 02.09.2017
"""


def my_split(string, sep=None, maxsplit=-1):

    split_list = []

    if sep == '':
        raise Exception('ValueError: empty separator')

    if sep:
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
    else:
        for el in string:
            split_list.append(el)

    return split_list

# tests
string_1 = 'mic___hal___mod___lin___ski'
sep_1 = 'mic'
# sep_1 = 'ski'  # not equal!
# sep_1 = '-'
# sep_1 = '--'
# sep_1 = '---'
# sep_1 = '----'
print(my_split(string_1, sep_1))
print(string_1.split(sep_1))
