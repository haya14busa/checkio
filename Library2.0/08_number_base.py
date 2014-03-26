#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FILE: 08_number_base.py
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

# http://www.checkio.org/mission/number-radix/


def number_base(str_number, radix):
    '''
    class int(object)
     |  int(x=0) -> int or long
     |  int(x, base=10) -> int or long
     |
     |  Convert a number or string to an integer, or return 0 if no arguments
     |  are given.  If x is floating point, the conversion truncates towards zero.
     |  If x is outside the integer range, the function returns a long instead.
     |
     |  If x is not a number or if base is given, then x must be a string or
     |  Unicode object representing an integer literal in the given base.  The
     |  literal can be preceded by '+' or '-' and be surrounded by whitespace.
     |  The base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to
     |  interpret the base from the string as an integer literal.
     |  >>> int('0b100', base=0)
     |  4
    '''
    try:
        return int(str_number, base=radix)
    except ValueError:
        return -1


def number_base_small(*args):
    try: return int(*args)
    except ValueError: return -1


def checkio(str_number, radix):
    return number_base(str_number, radix)
    # return number_base(str_number, radix)


if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
    print('All done')
