class SearchAlgo:
    @staticmethod
    def verify(index):
        if index is None:
            print(f'Target not found')
        else:
            print(f'Target found at index {index}')

    @staticmethod
    def linear_search(array, target):
        """ Return the first index of target element in the array using sequential search"""
        for i in range(0, len(array)):
            if array[i] == target:
                return i

    @staticmethod
    def linear_search_all_elements(array, target):
        """ Return the all indexes of target element in the array """

        for i in range(0, len(array)):
            if array[i] == target:
                yield i

    @staticmethod
    def binary_search(array, target):
        """ Return the first index of target element in the array using binary search """

        array = sorted(array)
        start, last = 0, len(array)-1

        while start <= last:
            mid = (start+last)//2

            if array[mid] == target:
                return mid
            elif array[mid] < target:
                start = mid+1
            else:
                last = mid-1

    @staticmethod
    def binary_search_recursive(array, start, last, target):
        """ Return the first index of target element in the array using binary search """

        if len(array) == 0:
            return None

        mid = (start+last)//2
        if array[mid] == target:
            return mid

        elif array[mid] < target:
            return SearchAlgo.binary_search_recursive(array, mid+1, last, target)

        else:
            return SearchAlgo.binary_search_recursive(array, start, mid-1, target)


# # ------------------ RUN EXAMPLES --------------
#
# res = SearchAlgo.linear_search([3, 4, 5, 6, 1, 3, 7], 3)
# SearchAlgo.verify(res)
#
# res = list(SearchAlgo.linear_search_all_elements([3, 4, 5, 6, 1, 3, 7], 3))
# SearchAlgo.verify(res)
#
# res = SearchAlgo.binary_search([1, 3, 3, 4, 5, 6, 7], 6)
# SearchAlgo.verify(res)
#
# arr = [1, 3, 3, 4, 5, 6, 7]
# res = SearchAlgo.binary_search_recursive(arr, 0, len(arr)-1, 5)
# SearchAlgo.verify(res)
