#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FILE: 06_the_end_of_other.py
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

# http://www.checkio.org/mission/end-of-other/


# Clear
def is_contain_end_of_other(words_set):
    if len(words_set) < 2:
        return False
    for suffix in words_set:
        # set('deco') # -> set(['c', 'e', 'd', 'o'])
        # {'deco'} # -> set(['deco'])
        for word in words_set - {suffix}:
            if word.endswith(suffix):
                return True
    return False


# Do not use `set`
def is_contain_end_of_other_list(words_set):
    words_list = list(words_set)
    for suffix in words_list:
        for word in words_list:
            if suffix != word and len(suffix) < len(word) \
                    and suffix == word[-len(suffix):]:
                return True
    return False


def checkio(words_set):
    # return is_contain_end_of_other(words_set)
    return is_contain_end_of_other_list(words_set)

if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
    print('All done')
