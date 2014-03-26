#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FILE: 09_common_words.py
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
# http://www.checkio.org/mission/common-words/


def get_common_word_from_2_csv(csv1, csv2):
    '''
     |  split(...)
     |      S.split([sep [,maxsplit]]) -> list of strings
     |
     |      Return a list of the words in the string S, using sep as the
     |      delimiter string.  If maxsplit is given, at most maxsplit
     |      splits are done. If sep is not specified or is None, any
     |      whitespace string is a separator and empty strings are removed
     |      from the result.

    sorted(...)
        sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list

    class set(object)
     |  set() -> new empty set object
     |  set(iterable) -> new set object
     |
     |  Build an unordered collection of unique elements.
     |
     |  __rand__(...)
     |      x.__rand__(y) <==> y&x
     |
     |  intersection(...)
     |      Return the intersection of two or more sets as a new set.
     |
     |      (i.e. elements that are common to all of the sets.)
    '''
    word_set_1 = set(csv1.split(','))
    word_set_2 = set(csv2.split(','))
    return ','.join(sorted(list(word_set_1 & word_set_2)))
    # return ','.join(sorted(list(word_set_1.__rand__(word_set_2))))
    ''' intersection() '''
    # return ','.join(sorted(list(word_set_1.intersection(word_set_2))))


def checkio(first, second):
    return get_common_word_from_2_csv(first, second)


if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
    print('All done')
