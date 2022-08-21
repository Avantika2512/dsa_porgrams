from unittest import TestCase
from algorithms.utils.linked_list import Node
from algorithms.singly_linked_list import SinglyLinkedList
from algorithms.doubly_linked_list import DoublyLinkedList


class LinkedListTest(TestCase):
    def assert_is_empty(self, ll):
        print('\nTesting Emptiness of Linked List\n')
        self.assertIsNotNone(ll.head)

        ll.clear()
        self.assertTrue(ll.is_empty())

    def assert_size(self, ll):
        print('\nTesting Size of Linked List\n')
        self.assertIsInstance(ll.size(), int)

    def assert_append(self, ll):
        print('\nTesting Insertion at End of Linked List\n')
        if ll.is_empty():
            self.assertEqual(ll.size(), 0)

        for i in range(-3, 5):
            ll.append(i)

    def assert_prepend(self, ll):
        print('\nTesting Insertion at Start of Linked List\n')
        if ll.is_empty():
            self.assertEqual(ll.size(), 0)

        for i in range(-3, 1):
            ll.prepend(i)

    def assert_insert(self, ll):
        print('\nTesting Insertion at index i of Linked List\n')
        if ll.is_empty():
            self.assertEqual(ll.size(), 0)

        nums = [1, 2, 3, 4, 5, 6]
        # insert at beginnning
        ll.insert(nums[0], 0)
        ll.insert(nums[1], 0)

        # insert at end
        ll.insert(nums[2], -1)
        ll.insert(nums[3], -1)

        # insert in between
        ll.insert(nums[4], 1)
        ll.insert(nums[5], 2)

    def assert_pop(self, ll):
        print('\nTesting Removal of node from end of Linked List\n')
        length = ll.size()

        self.assertNotEqual(length, 0)
        self.assertIsInstance(ll.pop(), Node)
        self.assertEqual(ll.size(), length - 1)

    def assert_pop_first(self, ll):
        print('\nTesting Removal of node from start of Linked List\n')
        length = ll.size()

        self.assertNotEqual(length, 0)
        self.assertIsInstance(ll.pop_first(), Node)
        self.assertEqual(ll.size(), length - 1)

    def assert_remove(self, ll):
        print('\nTesting Removal of node from index i of Linked List\n')
        length = ll.size()

        self.assertNotEqual(length, 0)
        self.assertIsInstance(ll.remove(1), Node)
        self.assertEqual(ll.size(), length - 1)

    def assert_all_operations(self, ll):
        # ------------------ RUN EXAMPLES --------------
        print("\nTesting All Operations\n")
        # inserting at end
        self.assertIsNone(ll.append(10))  # append operation returns nothing just adds to the list
        ll.append(20)
        ll.append(30)

        # inserting at beginning of list
        self.assertIsNone(ll.prepend(-10))  # prepend operation returns nothing just adds to the list
        ll.prepend(-20)
        ll.prepend(-30)

        # inserting at index i,
        self.assertIsNone(ll.insert(-40, 0))  # insert operation returns nothing just adds to the list
        ll.insert(40, ll.size())
        ll.insert(0, ll.size() // 2)

        node, pos = ll.search(40)
        self.__asert_search_validity(node, pos, ll)

        node, pos = ll.search(-30)
        self.__asert_search_validity(node, pos, ll)

        node, pos = ll.search(-50)
        self.__asert_search_validity(node, pos, ll)

        node, pos = ll.search(100)
        self.__asert_search_validity(node, pos, ll)

        node = ll.pop()
        self.__assert_pop(node)

        node = ll.pop_first()
        self.__assert_pop(node)

        node = ll.remove(3)
        self.__assert_pop(node)

        ll = ll.sort()

        self.assertIsInstance(ll, type(ll))
        self.assertIsInstance(ll.head, type(ll.head))
        self.assertIsInstance(ll.size(), int)

    def __assert_pop(self, node):
        if node:
            self.assertIsInstance(node, Node)
        else:
            self.assertIsNone(node)

    def __asert_search_validity(self, node, pos, ll):
        if node:
            self.assertIsInstance(node, Node)
            self.assertIn(pos, list(range(ll.size())))
        else:
            self.assertIsNone(node)
            self.assertIsNone(pos)


class SinglyLinkedListTest(LinkedListTest):
    def setUp(self):
        print('Creating Singly Linked List')
        self.ll = SinglyLinkedList()
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        print(f"At Beginning: {self.ll} | {self.ll.size()} Nodes")

    def test_is_empty(self):
        self.assert_is_empty(self.ll)

    def test_size(self):
        self.assert_size(self.ll)

    def test_append(self):
        self.assert_append(self.ll)

    def test_prepend(self):
        self.assert_prepend(self.ll)

    def test_insert(self):
        self.assert_insert(self.ll)

    def test_pop(self):
        self.assert_pop(self.ll)

    def test_pop_first(self):
        self.assert_pop_first(self.ll)

    def test_remove(self):
        self.assert_remove(self.ll)

    def test_all_operations(self):
        self.assert_all_operations(self.ll)

    def tearDown(self):
        print(f"At End: {self.ll} | {self.ll.size()} Nodes")
        print('Deleting Singly Linked List\n')
        del self.ll


class DoublyLinkedListTest(SinglyLinkedListTest):
    def setUp(self):
        print('Creating Doubly Linked List')
        self.ll = DoublyLinkedList()
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        print(f"At Beginning: {self.ll} | {self.ll.size()} Nodes")
