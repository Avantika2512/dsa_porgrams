from dsa_algos.utils.util import validate_array_instance


class SortAlgo:
    @staticmethod
    def merge_sort(array):
        """
        Returns the sorted array in O(n logn) time and O(n) space
        Divide and Conquer approach
        :param array:
        :return:
        """

        def _merge(left, right):
            """
            merge 2 distinctly sorted arrays into 1 and return the new array
            :param left:
            :param right:
            :return:
            """
            array = []
            i, j = 0, 0

            while i < len(left) and j < len(right):
                if left[i] <= right[i]:
                    # add left array's element to the new array which will turn out to be sorted post execution
                    # and move 1 index fwd on left array
                    array.append(left[i])
                    i += 1
                else:
                    # Do a similar thing, append the right arrays's element and move 1 index fwd on right arr
                    array.append(right[j])
                    j += 1

            # Still some elements in left sorted array remain to be processed &
            # right array is fully processed, add the left array elements in new array
            while i < len(left):
                array.append(left[i])
                i += 1

            # Right array remaining elements to be added to new array
            # left array is fully processed
            while j < len(right):
                array.append(right[j])
                j += 1

            return array

        validate_array_instance(array)

        if len(array) <= 1:
            # only 1 element in the list, it's considered to be sorted on it's own
            return array

        mid = len(array)//2
        left = SortAlgo.merge_sort(array[:mid])
        right = SortAlgo.merge_sort(array[mid:])

        array = _merge(left, right)

        return array
