class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node {self.data}"


class LinkedListUtil:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Check if Linked List is empty or not
        :return: bool
        """
        return self.head is None

    def size(self, circular=False):
        """
        Returns the length of the linked list - O(n) time
        :return: int
        """
        current, last = self.head, None
        count = 0
        if circular:
            last = self.head

        while current:
            count += 1
            if current.next == last:
                break
            else:
                current = current.next
        return count

    def clear(self):
        """
        Empty the linked list
        :return: SinglyLinkedList
        """
        current = self.head
        while current:
            self.pop_first()
            current = self.head

        return self

    def __repr__(self):
        nodes = []
        current = self.head

        if hasattr(current, 'prev'):
            delim = '<->'
        else:
            delim = '->'

        while current:
            if current is self.head:
                nodes.append(f"[Head {current}]")
            elif current.next is None:
                nodes.append(f"[Tail {current}]")
            else:
                nodes.append(f"[{current}]")
            current = current.next

        return "None->" + delim.join(nodes) + "->None"
