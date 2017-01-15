def flatten(iterable, shallow=False):
    if shallow:
        raise NotImplementedError

    try:
        for sublist in iterable:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield iterable

