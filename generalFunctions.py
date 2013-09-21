#standard imports here
from pprint import pprint
#import utilities
from utilities.docInherit import *


def isSet(array, *index):
    """
    check if array contains element by given index (can be multidimensional)
    :param array: 
    :param index:
    """
    #simply try to reference element under given index
    try:
        element = array[index[0]]
    except IndexError:
        #fail if such index is not set
        return False
    except KeyError:
        #fail if such key is not set
        return False
    else:
        #in case of multidimensional index, check recursively
        if len(index) > 1:
            return isSet(element, *index[1:])
        #if desired depth is reached, we're done
        else:
            return True


def getKeyInput():
    """
    read pressed key
    """
    import sys
    #for now take first character from given line
    return sys.stdin.readlines(1)[0][0]


def charRange(startChar, stopChar):
    """
    generate characters from startChar to stopChar
    :param startChar: first character to be generated
    :param stopChar: last character to be generated
    """
    #if characters out of range (a-z)
    if startChar < 'a':
        startChar = 'a'
    if stopChar > 'z':
        stopChar = 'z'
    #generate characters in given range
    for c in range(ord(startChar), ord(stopChar)+1):
        yield chr(c)


def charGen(length=26):
    """
    generate length of characters starting from 'a'
    :param length: number of characters to generate (max 26, which corresponds to a-z)
    """
    #cast parameters to fit charRange() function
    return charRange('a', chr(ord('a') + length - 1))


def directionToVector(direction):
    """
    translate direction in form of string into vector
    :param direction: literal geographical direction, combination of N, W, S, E
    """
    vector = [0, 0]
    if direction.find("N") > -1:
        vector[1] = 1
    if direction.find("S") > -1:
        vector[1] = -1
    if direction.find("E") > -1:
        vector[0] = 1
    if direction.find("W") > -1:
        vector[0] = -1
    return vector