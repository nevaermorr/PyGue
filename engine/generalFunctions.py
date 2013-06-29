#standard imports here
from pprint import pprint


def isSet(array, *index):
    """
    checking if array contains element by given index (can be multidimensional)
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
        #if we reached desired depth, we're done
        else:
            return True

from functools import wraps


class DocInherit(object):
    """
    Docstring inheriting method descriptor
    The class itself is also used as a decorator
    taken from http://code.activestate.com/recipes/576862/
    """

    def __init__(self, mthd):
        self.mthd = mthd
        self.name = mthd.__name__

    def __get__(self, obj, cls):
        if obj:
            return self.get_with_inst(obj, cls)
        else:
            return self.get_no_inst(cls)

    def get_with_inst(self, obj, cls):

        overridden = getattr(super(cls, obj), self.name, None)

        @wraps(self.mthd, assigned=('__name__', '__module__'))
        def f(*args, **kwargs):
            return self.mthd(obj, *args, **kwargs)

        return self.use_parent_doc(f, overridden)

    def get_no_inst(self, cls):

        for parent in cls.__mro__[1:]:
            overridden = getattr(parent, self.name, None)
            if overridden: break

        @wraps(self.mthd, assigned=('__name__', '__module__'))
        def f(*args, **kwargs):
            return self.mthd(*args, **kwargs)

        return self.use_parent_doc(f, overridden)

    def use_parent_doc(self, func, source):
        if source is None:
            raise NameError(("Can't find '%s' in parents" % self.name))
        func.__doc__ = source.__doc__
        return func

doc_inherit = DocInherit