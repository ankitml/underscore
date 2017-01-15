import unittest
from underscore import array as _
from itertools import chain


class TestFlatten(unittest.TestCase):

    def test_flat_list(self):
        l = [1,2,3,4]
        flat = list(_.flatten(l))
        self.assertEqual(l,flat)

    def test_flat_generator(self):
        l = range(0, 10)
        flat = _.flatten(range(0,10))
        self.assertEqual(list(l), list(flat))

    def test_single_nest_list(self):
        l = [1, 2, 3, [4]]
        flat = list(_.flatten(l))
        self.assertEqual([1,2,3,4], flat)
        l = [[1,2,3], [4,5,6], [7,8,9]]
        flat = list(_.flatten(l))
        self.assertEqual(flat, [1,2,3,4,5,6,7,8,9])

    def test_single_nest_generator(self):
        l = [range(0,3), range(3,6), range(6,9)]
        flat = list(_.flatten(l))
        self.assertEqual(flat, [0,1,2,3,4,5,6,7,8])

        l = chain(range(0,3), range(3,6), range(6,9))
        flat = list(_.flatten(l))
        self.assertEqual(flat, [0,1,2,3,4,5,6,7,8])

    def test_deep_nested_list(self):
        l = [[1,2], [3,4], [[5, 6], 7, 8]]
        flat = list(_.flatten(l))
        self.assertEqual(flat, [1,2,3,4,5,6,7,8])

    def test_deep_nested_generator(self):
        gen = range(0,3)
        squared_gen = lambda : map(lambda x: x*x, range(0,3))
        nested_gen = chain(gen, gen)
        nested_gen2 = chain(squared_gen(), squared_gen())
        deep_nested_generator = chain(nested_gen, nested_gen2)

        flat = list(_.flatten(deep_nested_generator))
        self.assertEqual(flat, [0,1,2,0,1,2,0,1,4,0,1,4])
        print(flat)





if __name__ == "__main__":
    unittest.main()
