import unittest
from src import main as _
from types import GeneratorType
from unittest.mock import patch
from .helpers import side_effects_fn


class TestEach(unittest.TestCase):

    @patch('tests.helpers.side_effects_fn')
    def test_list_return(self, patched_fn):
        l = [1,10,100]
        ret = _.each(l, side_effects_fn)
        patched_fn.assert_not_called()
        list(ret)
        # TODO fails following assertion somehow
        # patched_fn.assert_any_call()


class TestMap(unittest.TestCase):

    def test_simple_list(self):
        l = [1, 2, 3]
        triple_l = _.map(l, lambda x: 3*x)
        self.assertEqual(list(triple_l), [3,6,9])


class TestReduce(unittest.TestCase):
    
    def test_simple_list(self):
        l = [1, 2, 3]
        total = _.reduce(l, lambda m, v: m+v, 0)
        self.assertEqual(total, 6)
        # twisted_total = _.reduce(l, lambda m, v, i: m + v*i)



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
