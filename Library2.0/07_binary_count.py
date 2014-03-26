#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FILE: 07_binary_count.py
# AUTHOR: haya14busa
# License: MIT license
#
#     Permission is hereby granted, free of charge, to any person obtaining
#     a copy of this software and associated documentation files (the
#     "Software"), to deal in the Software without restriction, including
#     without limitation the rights to use, copy, modify, merge, publish,
#     distribute, sublicense, and/or sell copies of the Software, and to
#     permit persons to whom the Software is furnished to do so, subject to
#     the following conditions:
#
#     The above copyright notice and this permission notice shall be included
#     in all copies or substantial portions of the Software.
#
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#     OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#     MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#     CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#     TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#     SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#=============================================================================

# http://www.checkio.org/mission/binary-count/


def count_one_in_binary_number(number):
    '''
    bin(...)
        bin(number) -> string

        Return the binary representation of an integer or long integer.

    class list(object)
     |  count(...)
     |      L.count(value) -> integer -- return number of occurrences of value
    '''
    return bin(number).count('1')


oneliner = lambda n: bin(n).count('1')


def checkio(number):
    return count_one_in_binary_number(number)
    # return oneliner(number)

if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
    print('All done')
