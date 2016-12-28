import unittest
from src import main as u


class TestEach(unittest.TestCase):

    def test_list_return(self):
        l = [1,10,100]
        fn = lambda v,k,l:print(v,k,l)
        ret = u.each(l, fn)
        self.assertEqual(list(ret), l)

    # todo test side effects of the function being called

class TestFind(unittest.TestCase):

    def test_simple(self):
        l = [1,10,100]
        condition = lambda item: item % 10 == 0
        first_divisible_by_10 = u.find(condition, l)
        self.assertEqual(first_divisible_by_10.__next__(), 10)



if __name__ == "__main__":
    unittest.main()
