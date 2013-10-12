# standard imports here
from pprint import pprint

# import utilities
from utilities.docInherit import *


def is_set(array, *index):
    """
    check if array contains element by given index (can be multidimensional)
    :param array: 
    :param index:
    """
    # simply try to reference element under given index
    try:
        element = array[index[0]]
    except IndexError:
        # fail if such index is not set
        return False
    except KeyError:
        # fail if such key is not set
        return False
    else:
        # in case of multidimensional index, check recursively
        if len(index) > 1:
            return is_set(element, *index[1:])
        # if desired depth is reached, we're done
        else:
            return True


def get_key_input():
    """
    read pressed key
    """
    import sys
    # for now take first character from given line
    return sys.stdin.readlines(1)[0][0]


def char_range(start_char, stop_char):
    """
    generate characters from startChar to stopChar
    :param start_char: first character to be generated
    :param stop_char: last character to be generated
    """
    # if characters out of range (a-z)
    if start_char < 'a':
        start_char = 'a'
    if stop_char > 'z':
        stop_char = 'z'
    # generate characters in given range
    for c in range(ord(start_char), ord(stop_char)+1):
        yield chr(c)


def char_gen(length=26):
    """
    generate length of characters starting from 'a'
    :param length: number of characters to generate (max 26, which corresponds to a-z)
    """
    # cast parameters to fit char_range() function
    return char_range('a', chr(ord('a') + length - 1))