import unittest
from src import arrays as _


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



if __name__ == "__main__":
    unittest.main()
