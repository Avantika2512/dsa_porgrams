class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node: {self.data}"


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        Returns the length of the linked list - O(n) time
        :return:
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next

        return count

    # INSERTION OPERATIONS
    def append(self, data):
        """
        Insert data at the end of the linked list the length of the linked list - O(n) time
        :param data: any object - int, string, list etc.
        :return:
        """
        node = Node(data)

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
        node = Node(data)

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

        if at_index > length or at_index < -(length+1):
            raise Exception(f'UNABLE TO INSERT: {at_index} is not in range -{length+1} to {length} inclusive')

        elif at_index == 0 or at_index == -(length+1):  # same as insert at beginning
            return self.prepend(data)

        elif at_index == length or at_index == -1:  # same as insert at end
            return self.append(data)

        else:  # somewhere in the list except at end or beginning
            current = self.head
            index_traversed = -1
            while current.next:
                index_traversed += 1
                if index_traversed == at_index-1:
                    # stop at 1 previous index of the data so that insert becomes easy
                    # as there is no prev pointer like in doubly linked list
                    break

                current = current.next

            node = Node(data)
            node.next = current.next
            current.next = node

    # DELETION OPERATIONS
    def pop(self):
        """
        Removes the last node of the linked list and returns it
        :return:
        """
        current = self.head
        next_node = self.head.next
        while current.next and next_node.next:
            current = next_node
            next_node = next_node.next
        current.next = None
        return next_node

    def pop_first(self):
        """
        Removes the first node of the linked list and returns it
        :return:
        """
        current = self.head
        self.head = current.next
        return current

    def remove(self, from_index):
        """
        Removes the node from the specified index of the linked list and returns it
        :return:
        """
        """
                Insert data at the end of the linked list the length of the linked list - O(n) time
                :param data: any object - int, string, list etc.
                :param at_index: int
                :return:
                """
        length = self.size()

        if from_index > length-1 or from_index < -length:
            raise Exception(f'UNABLE TO REMOVE: {from_index} is not in range -{length} to {length-1} inclusive')

        elif from_index == 0 or from_index == -length:  # same as remove from beginning
            return self.pop_first()

        elif from_index == length-1 or from_index == -1:  # same as remove from end
            return self.pop()

        else:  # somewhere in the list except at end or beginning
            current = self.head
            index_traversed = -1
            while current.next:
                index_traversed += 1
                if index_traversed == from_index - 1:
                    # stop at 1 previous index of the data so that insert becomes easy
                    # as there is no prev pointer like in doubly linked list
                    break

                current = current.next
            removed = current.next
            current.next = removed.next
            return removed

    # SEARCH OPERATIONS
    def search(self, target):
        """
        Returns the target node if found. Uses binary search - O(n log(n))
        :param target: any object string, list, int etc.
        :return:
        """
        def mid_node(start, end):
            # for every 2 node moves of the fast pointer
            # slow pointer moves 1 node ahead

            slow = start
            fast = start.next

            while fast != end:
                fast = fast.next
                if fast != end:
                    slow = slow.next
                    fast = fast.next
            return slow

        start = self.head
        end = None

        while True:
            if (end == start) or start is None:
                # reached the start or end of the linked list but target is not found
                return None

            mid = mid_node(start, end)

            if mid.data == target:
                return mid
            elif mid.data < target:
                start = mid.next
            else:
                end = mid

    # SORTING OPERATIONS
    def sort(self, asc=True):
        """
        Sorts and returns a new linked list object. Not Very efficient way to sort though. Need to make better.
        :param asc: bool
        :return: self
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

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head {current}]")
            elif current.next is None:
                nodes.append(f"[Tail {current}]")
            else:
                nodes.append(f"[{current}]")
            current = current.next
        return "->".join(nodes)


# # ------------------ RUN EXAMPLES --------------
#
# sll = SinglyLinkedList()
#
# # inserting at end
# sll.append(10)
# sll.append(20)
# sll.append(30)
#
# # inserting at beginning of list
# sll.prepend(-10)
# sll.prepend(-20)
# sll.prepend(-30)
#
# # inserting at index i,
# sll.insert(-40, 0)
# sll.insert(40, sll.size())
# sll.insert(0, sll.size()//2)
#
# print(sll)
# print(sll.size())
#
# print(sll.search(40))
# print(sll.search(-30))
# print(sll.search(-50))
# print(sll.search(100))
#
# print(sll.pop())
# print(sll.pop_first())
# print(sll)
# print(sll.remove(3))
# print(sll)
# print(sll.size())
# sll.append(-40)
# sll = sll.sort()
