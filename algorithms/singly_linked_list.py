from algorithms.utils.linked_list import LinkedListUtil, Node


class SinglyNode(Node):
    def __init__(self, data):
        super(SinglyNode, self).__init__(data)


class SinglyLinkedList(LinkedListUtil):
    def __init__(self):
        """Initialise an empty linked list i.e. self.head = None"""
        super(SinglyLinkedList, self).__init__()

    # INSERTION OPERATIONS
    def append(self, data):
        """
        Insert data at the end of the linked list the length of the linked list - O(n) time
        :param data: any object - int, string, list etc.
        :return:
        """
        node = SinglyNode(data)

        # if SLL is empty add the first node and return
        if self.is_empty():
            self.head = node
            return

        # if not, traverse to the end of the list and add it there
        current = self.head
        while current.next:
            current = current.next

        current.next = node

    def prepend(self, data):
        """
        Insert data at the beginning of the linked list the length of the linked list - O(1) time
        :param data: any object - int, string, list etc.
        :return:
        """
        node = SinglyNode(data)

        # if SLL is empty add the first node and return
        if self.is_empty():
            self.head = node
            return

        node.next = self.head
        self.head = node

    def insert(self, data, at_index):
        """
        Insert data at the end of the linked list the length of the linked list - O(n) time
        :param data: any object - int, string, list etc.
        :param at_index: int
        :return:
        """
        length = self.size()

        if at_index == 0 or at_index <= -(length+1):  # same as insert at beginning
            return self.prepend(data)

        elif at_index == -1 or at_index >= length:  # same as insert at end
            return self.append(data)

        else:  # somewhere in the list except at end or beginning
            current = self.head
            index_traversed = 0
            while current.next:
                if index_traversed == at_index-1:
                    # stop at 1 previous index of the data so that insert becomes easy
                    # as there is no prev pointer like in doubly linked list
                    break
                index_traversed += 1
                current = current.next

            node = SinglyNode(data)
            node.next = current.next
            current.next = node

    # DELETION OPERATIONS
    def pop(self):
        """
        Removes the last node of the linked list and returns it
        :return: SinglyNode
        """
        if self.is_empty():
            return None

        current = self.head
        next_node = current.next

        while current.next and next_node and next_node.next:
            current = next_node
            next_node = next_node.next
        current.next = None

        if next_node:
            return next_node
        else:
            return self.pop_first()

    def pop_first(self):
        """
        Removes the first node of the linked list and returns it
        :return: SinglyNode
        """
        if self.is_empty():
            return None
        current = self.head
        self.head = current.next
        current.next = None
        return current

    def remove(self, from_index):
        """
        Removes the node from the specified index of the linked list and returns it
        :return: SinglyNode
        """

        if self.is_empty():
            return None

        length = self.size()

        if from_index == 0 or from_index <= -length:  # same as remove from beginning
            return self.pop_first()

        elif from_index == -1 or from_index >= length-1:  # same as remove from end
            return self.pop()

        else:  # somewhere in the list except at end or beginning
            current = self.head
            index_traversed = 0
            while current.next:
                if index_traversed == from_index - 1:
                    # stop at 1 previous index of the data so that insert becomes easy
                    # as there is no prev pointer like in doubly linked list
                    break
                index_traversed += 1
                current = current.next

            removed = current.next
            current.next = removed.next
            removed.next = None
            return removed

    # SEARCH OPERATIONS
    def search(self, target):
        """
        Returns the target node, and it's position if found. Uses binary search - O(n log(n))
        :param target: any object string, list, int etc.
        :return: SinglyNode, int
        """
        def mid_node(start, end, pos):
            # for every 2 node moves of the fast pointer
            # slow pointer moves 1 node ahead

            slow = start
            fast = start.next

            while fast != end:
                fast = fast.next
                if fast != end:
                    pos += 1
                    slow = slow.next
                    fast = fast.next
            return slow, pos

        start = self.head
        end = None
        pos = 0

        while True:
            if (end == start) or start is None:
                # reached the start or end of the linked list but target is not found
                return None, None

            mid, pos = mid_node(start, end, pos)

            if mid.data == target:
                return mid, pos
            elif mid.data < target:
                pos += 1
                start = mid.next
            else:
                pos -= 1
                end = mid

    # SORTING OPERATIONS
    def sort(self, asc=True):
        """
        Sorts and returns a new linked list object. Not Very efficient way to sort though. Need to make better.
        :param asc: bool
        :return: SinglyLinkedList
        """
        nodes_data = []
        current = self.head
        while current:
            nodes_data.append(current.data)
            current = current.next
        if asc:
            nodes_data = sorted(nodes_data, reverse=False)
        else:
            nodes_data = sorted(nodes_data, reverse=True)

        self.head = None
        for data in nodes_data:
            self.append(data)

        return self


sll = SinglyLinkedList()
sll.append(4)
sll.append(5)
sll.append(4)
print(sll)