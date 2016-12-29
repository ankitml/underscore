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


class TestFilter(unittest.TestCase):
    pass


class TestWhere(unittest.TestCase):
    pass


class TestFindWhere(unittest.TestCase):
    pass


class TestReject(unittest.TestCase):
    pass


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
    pass


class TestCountBy(unittest.TestCase):
    pass


class TestShuffle(unittest.TestCase):
    pass


class TestSample(unittest.TestCase):
    pass


class TestSize(unittest.TestCase):
    pass


class TestPartition(unittest.TestCase):

    def test_simple_list(self):
        l = [1,2,3,4,5,6,7,8,9]
        is_even = lambda x: x % 2 == 0
        evens, not_evens = _.partition(l, is_even)
        self.assertIsInstance(evens, GeneratorType)
        self.assertIsInstance(not_evens, GeneratorType)
        self.assertEqual(list(evens), [2,4,6,8])
        self.assertEqual(list(not_evens), [1,3,5,7,9])



if __name__ == "__main__":
    unittest.main()
