from dsa_algos.utils.util import validate_array_instance


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
        validate_array_instance(array)
        res = list(filter(lambda x:
                           x is not None,
                           list(map(lambda tup:
                                    tup[0] if tup[1]==target else None,
                                    enumerate(array)
                                    )
                                )
                           )
                    )
        return res[0] if res else None

    @staticmethod
    def linear_search_all_elements(array, target):
        """ Return the all indexes of target element in the array """

        validate_array_instance(array)
        res = list(filter(lambda x:
                           x is not None,
                           list(map(lambda tup:
                                    tup[0] if tup[1]==target else None,
                                    enumerate(array)
                                    )
                                )
                           )
                    )

        return res if res else None

    @staticmethod
    def binary_search(array, target):
        """ Return the first index of target element in the array using binary search """

        validate_array_instance(array)
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
        validate_array_instance(array)

        if len(array) == 0:
            return None

        mid = (start+last)//2
        if array[mid] == target:
            return mid

        elif array[mid] < target:
            return SearchAlgo.binary_search_recursive(array, mid+1, last, target)

        else:
            return SearchAlgo.binary_search_recursive(array, start, mid-1, target)
