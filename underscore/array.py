from iterrools import islice


def first(iterable, n=1):
    """
    Returns the first element of an iterable. Passing n will return the first n elements of the iterable.
    Does not modify the original iterator, copies it into a new generator. So if the iterable passed is
    a generator it will not be consumed.
    """
    return islice(iterable, 0, n)

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


