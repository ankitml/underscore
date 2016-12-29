import unittest
from src import main as u


class TestEach(unittest.TestCase):

    def test_list_return(self):
        l = [1,10,100]
        fn = lambda v,k,l:print(v,k,l)
        ret = u.each(l, fn)
        self.assertEqual(list(ret), l)
    # todo test side effects of the function being called


class TestMap(unittest.TestCase):
    pass


class TestReduce(unittest.TestCase):
    pass


class TestReduceRight(unittest.TestCase):
    pass


class TestFind(unittest.TestCase):

    def test_simple(self):
        l = [1,10,100]
        condition = lambda item: item % 10 == 0
        first_divisible_by_10 = u.find(condition, l)
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
    pass



if __name__ == "__main__":
    unittest.main()
