import itertools
import functools
from types import GeneratorType



def each(array, iteratee):
    """
    Iterates over a list, yielding each element in turn to an iteratee function. 
    Each invocation of iteratee is called with three arguments: (element, index, list). 

    params: array, function/lambda
    array: the list whose elements will will be passed on the function one by one. This can be a generator as well yielding elements one by one. 
    function -> a function or lambda that takes three inputs, element of the list, index of element, array

    Returns a generator of all the elements, hence can be chained.

    Example: 
    >>> array = [1,10,100]
    >>> iteratee1 = lambda val, key, arr: print(val)
    >>> iteratee2 = lambda val, key, arr: print(key)
    >>> lazy_each_object = _.each(_.each(array, iteratee1), iteratee2)
    This lazy object is a generator and is not executed yet. This can be done wither by casting generator into a list, which returns the original array or iterating over it.
    >>> list(lazy_each_object)
    >>> 1
    >>> 0
    >>> 10
    >>> 1
    >>> 100
    >>> 2
    Note the order or execution. All the iteratees are finished first for an element before the next element takes over. This can be changed by casting into list before passing it to next _.each method.
    >>> not_so_lazy_each_object = list(_.each(list(_.each(array, iteratee1)), iteratee2))
    >>> 1
    >>> 10
    >>> 100
    >>> 0
    >>> 1
    >>> 2
    """
    # list, sets, tuples, generators
    for key,value in enumerate(array):
        iteratee(value,key,array)
        yield value


def map(array, iteratee):
    """
    Produces a new stream of values (generator) by mapping each value in array (list, set, tuple, generator) through a transformation function (iteratee). The iteratee is passed three arguments: the value, then the index (or key) of the iteration, and finally a reference to the entire list.
    """
    for index, item in enumerate(array):
        yield iteratee(item, index, array)


def reduce(array, iteratee, init=None):
    return functools.reduce(iteratee, array, init)


def reduce_right(array, iteratee, init=None):
    raise NotImplementedError("Reduce right is not compatible with generators")


def find(conditional, collection):
    """
    test if first argument is a conditional or not


    Looks through each value in the list, returning the first one that passes a truth test 
    (conditional). The function yields as soon as it finds an acceptable element, and doesn't traverse the entire list
    """
    for element in collection:
        if conditional(element):
            yield element
            break


def filter(array, conditional):
    """
     Looks through each value in the list, returning an array of all the values that pass a truth test (conditional). 
    """
    return filter(conditional, array)


def where(array, properties):
    """
     Looks through each value in the list, returning an array of all the values that contain all of the key-value pairs listed in properties. 
     params: array, properties
     array-> a list/generator of dictionaries
     properties-> key value pairs which need to be in a dictionary.
    """
    items_to_be_checked = properties.items()
    for dictionary in array:
        if not isinstance(dictionary, dict):
            raise TypeError('"array" should be a collection of dictionaries only')
        if items_to_be_checked <= dictionary.items():
            yield dictionary


def find_where(array, properties):
    """
     Looks through the list and returns the first value that matches all of the key-value pairs listed in properties. j
    """
    pass

reject = itertools.filterfalse
every = all
some = any
sort_by = sorted

def group_by(function, collection):
    """
     Splits a collection into sets, grouped by the result of running each value through iteratee. 
     If iteratee is a string instead of a function, groups by the property named by iteratee on each of the values. 
    """
    return itertools.groupby(collection, function)

