import unittest
from src import main as _
from types import GeneratorType


class TestEach(unittest.TestCase):

    def test_list_return(self):
        l = [1,10,100]
        fn = lambda v,k:print(v,k)
        ret = _.each(l, fn)
        # todo test side effects of the function being called


class TestMap(unittest.TestCase):
    pass


class TestReduce(unittest.TestCase):
    pass


class TestReduceRight(unittest.TestCase):
    pass


class TestFind(unittest.TestCase):

    def test_simple_list(self):
        l = [1,10,100]
        condition = lambda item: item % 10 == 0
        first_divisible_by_10 = _.find(l, condition)
        self.assertEqual(first_divisible_by_10.__next__(), 10)


class TestSelect(unittest.TestCase):

    def test_simple_list(self):
        l = [1,2,3,4,5,6]
        is_even = lambda x: x % 2 == 0
        evens = _.select(l, is_even)
        self.assertEqual(list(evens), [2,4,6])


class TestWhere(unittest.TestCase):
    pass


class TestFindWhere(unittest.TestCase):
    pass


class TestReject(unittest.TestCase):

    def test_simple_list(self):
        l = [1,2,3,4,5,6]
        is_even = lambda x: x % 2 == 0
        not_evens = _.reject(l, is_even)
        self.assertEqual(list(not_evens), [1,3,5])

class TestEvery(unittest.TestCase):
    pass


class TestSome(unittest.TestCase):
    pass


class TestContains(unittest.TestCase):
    pass


class TestInvoke(unittest.TestCase):
    pass


class TestPluck(unittest.TestCase):
    pass


class TestMax(unittest.TestCase):
    pass


class TestMin(unittest.TestCase):
    pass


class TestSortBy(unittest.TestCase):
    pass


class TestGroupBy(unittest.TestCase):
    pass


class TestIndexBy(unittest.TestCase):
    
    def test_simple_list_with_key(self):
        stooges = [
                    {"name": 'moe', "age": 40}, 
                    {"name": 'larry', "age": 50}, 
                    {"name": 'curly', "age": 60}
                  ]
        age_indexed_stooges = _.index_by(stooges, key='age')
        self.assertDictEqual(age_indexed_stooges, {
            40: {"name": 'moe', "age": 40},
            50: {"name": 'larry', "age": 50},
            60: {"name": 'curly', "age": 60}})

    def test_simple_list_with_key_func(self):
        stooges = [
                    {"name": 'moe', "age": 40}, 
                    {"name": 'larry', "age": 50}, 
                    {"name": 'curly', "age": 60}
                  ]
        age_indexed_stooges = _.index_by(stooges, key_func=lambda x: x.get('age'))
        self.assertDictEqual(age_indexed_stooges, {
            40: {"name": 'moe', "age": 40},
            50: {"name": 'larry', "age": 50},
            60: {"name": 'curly', "age": 60}})


def count_by(iterable, iteratee):
    """
    Think of it like a harry potter sorting hat, tells you final number of students in every group.
    Similar to group_by, instead of returning a list with every grouped_key, returns count of grouped elements only.

    params: array, iteratee
        iterable-> list, set, generator 
        iteratee-> a function or a lambda for grouping the elements

    Examples
    >>> _.count_by([1, 2, 3, 4, 5], lambda x: 'even' if x % 2 == 0 else 'odd')
    >>> {"odd": 3, "even": 2}
    """
    from collections import defaultdict
    d = defaultdict(lambda: 0)
    for item in iterable:
        key = iteratee(item)
        d[iteratee(item)] += 1
    return dict(d)


def shuffle(iterable):
    """
    Returns a shuffled copy of the list.
    Caution: DOes not work with unordered collections and generators

    params: iterable
        iterable -> list, sequenece, 


    Examples:
    >>> _.shuffle([1, 2, 3, 4, 5, 6]);
    >>> [4, 1, 6, 3, 5, 2]
    """
    from random import random
    return sorted(iterable, key=lambda x: random())


def sample(iterable, n_sample):
    """
     Produce a random sample from the list. Pass a number to return n random elements from the list. Otherwise a single random item will be returned. 

    CAUTION: Does not yet work with generators
    params: iterable, n_sample
        iterable -> list, sequenece, set, dictionary
        n_sample -> number of random samples to be taken from iterable

    TODO: implement walker's method. current one is too inefficient
    http://code.activestate.com/recipes/576564-walkers-alias-method-for-random-objects-with-diffe/
    Examples:
    >>> _.sample([1, 2, 3, 4, 5, 6])
    >>> [4]
    >>> _.sample([1, 2, 3, 4, 5, 6], 3)
    >>> [1, 6, 2]
    """
    try:
        length = len(iterable)
    except TypeError:
        raise TypeError("sample does not work well with generators")
    import random
    sampled = []
    iterable = list(iterable)
    for i in range(n_sample):
        chosen = random.choice(iterable)
        iterable.remove(chosen)
        sampled.append(chosen)
    return sampled


def size(iterable):
    """
    Returns the length of an iterable. 
    Caution: If this iterable is generator, this method would eat up the generator

    params: iterable
        iterable -> list, sequenece, set, dictionary, generator etc

    Examples:
    >>> gen = (i for i in range(0,10))
    >>> _.size(gen)
    >>> 10
    """
    try:
        return len(iterable)
    except TypeError:
        length = 0
        for i in iterable:
            length = length + 1
        return length


def partition(iterable, conditional):
    """
     Splits the iterable into two iterators: one whose elements all satisfy conditional and one whose elements all do not satisfy conditional.

     params: iterators, conditional
        iterable -> list, sequenece, set, dictionary, generator etc
        conditional -> a lambda or function that takes one input and returns a boolean

    Examples:
    >>> even, odd = _.partition([1,2,3,4,5,6,7,8,9], lambda x: x % 2 ==0)
    >>> list(even)
    >>> [2,4,6,8]
    >>> list(odd)
    >>> [1,3,5,7,9]
    """
    return select(iterable, conditional), reject(iterable, conditional)




class TestCountBy(unittest.TestCase):

    def test_simple_list(self):
        l = range(1,6)
        is_even_or_odd = lambda x: 'even' if x % 2 == 0 else 'odd'
        even_odd_counts = _.count_by(l, is_even_or_odd)
        self.assertDictEqual(even_odd_counts, {'even': 2, 'odd': 3})


class TestShuffle(unittest.TestCase):
    
    def test_simple_list(self):
        l = range(1, 7)
        shuffled = _.shuffle(l)
        temp = []
        for item in shuffled:
            self.assertIn(item, l)
            self.assertNotIn(item, temp)
            temp.append(item)


class TestSample(unittest.TestCase):

    def test_simple_list(self):
        l = range(1, 7)
        random_sample = _.sample(l, 1)
        self.assertIsInstance(random_sample, list)
        for i in random_sample:
            self.assertIn(i, l)
        two_random_samples = _.sample(l, 2)
        self.assertIsInstance(two_random_samples, list)
        for i in two_random_samples:
            self.assertIn(i, l)
        self.assertEqual(len(two_random_samples), 2)



class TestSize(unittest.TestCase):

    def test_simple_list(self):
        l = range(0,10)
        self.assertEqual(_.size(l), 10)


class TestPartition(unittest.TestCase):

    def test_simple_list(self):
        l = range(1, 10)
        is_even = lambda x: x % 2 == 0
        evens, not_evens = _.partition(l, is_even)
        self.assertEqual(list(evens), [2,4,6,8])
        self.assertEqual(list(not_evens), [1,3,5,7,9])



if __name__ == "__main__":
    unittest.main()
