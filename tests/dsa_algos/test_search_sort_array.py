from dsa_algos.search_array import SearchAlgo
from unittest import TestCase

class SearchAlgoTest(TestCase):
    def setUp(self):
        print('Start of Search Algo Tests')
        self.empty_array = []
        self.single_elem_array = [4]
        self.repeated_elem_array = [1,2,3,4,5,6,4]
        self.target = 4

    def test_linear_search(self):
        print('Testing Linear search')
        # Testing empty list
        self.assertIsNone(SearchAlgo.linear_search(self.empty_array, self.target))
        self.assertEqual(SearchAlgo.linear_search(self.single_elem_array, self.target), 0)

        # Testing non empty list
        self.assertEqual(SearchAlgo.linear_search_all_elements(self.repeated_elem_array, self.target), [3,6])

    def test_binary_search(self):
        print('Testing Binary search')
        # Testing empty list
        self.assertIsNone(SearchAlgo.binary_search(self.empty_array, self.target))
        self.assertEqual(SearchAlgo.binary_search(self.single_elem_array, self.target), 0)

        # Testing non empty list
        self.assertEqual(SearchAlgo.binary_search_recursive(self.repeated_elem_array, 0, len(self.repeated_elem_array),
                                                            self.target), 3)

        # testing exception
        num = 1
        with self.assertRaises(Exception):
            SortAlgo.merge_sort(num)

    def tearDown(self) -> None:
        del self
        print('End of Search Algo Tests')

