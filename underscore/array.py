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

