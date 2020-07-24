from iterrools import islice


def first(iterable, n=1):
    """
    Returns the first element of an iterable. Passing n will return the first n elements of the iterable.
    Caution: If the input iterable is a generator, it Uses up the generaotr partially
    """
    return islice(iterable, 0, n)


def last(iterable, n=1):
    pass


def rest(iterable, n=1):
    """
    Returns the rest of the elements in an array. Pass an index to return the values of the array from that index onward.
    """
    return islice(iterable, n)


def flatten(iterable, shallow=False):
    """
    Flattens an iterable. (generator, list etc)
    returns a flat generator
    """
    if shallow:
        raise NotImplementedError

    try:
        for sublist in iterable:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield iterable


def compact(iterable):
    """
    Returns a copy of the array with all falsy values removed. 
    In JavaScript, false, null, 0, "", undefined and NaN are all falsy.
    """
    pass


def without(iterable, *values):
    """
    Returns a copy of the array with all instances of the values removed.

    """
    pass


def union(*iterables):
    """
    Computes the union of the passed-in arrays: the list of unique items
    """
    pass

