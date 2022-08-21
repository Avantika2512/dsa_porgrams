## DSA ALGORITHMS 

BELOW TOPICS ARE COVERED ALONG WITH USAGE (Scroll to see) 

- SEARCHING (Linear, Binary)
- SORTING
- LINKED LIST (Singly, Doubly)
- STACK
- QUEUE
- TREES
- GRAPHS
- DYNAMIC PROGRAMMING
- SOME LEETCODE, HACKKERANK QUESTIONS TOO

### Installation
```bash
pip install git+https://github.com/Avantika2512/dsa_programs
```

### LINKED LIST
#### [Singly Linked List](/dsa_algos/singly_linked_list.py)

<details>
<summary>Usage Example</summary>

```python
from dsa_algos.singly_linked_list import SinglyLinkedList

# CREATE EMPTY LIST
sll = SinglyLinkedList()

# INSERT
sll.append(5)
sll.append(-5)
sll.prepend(10)
sll.prepend(100)
sll.insert(data=70, at_index=1)
sll.insert(data=100, at_index=-1)

# REMOVE
sll.pop()
sll.pop_first()
sll.remove(from_index=2)

# SEARCH 
sll.search(10)
sll.search(99)

# SORT
sll.sort()

# PRINT
print(sll)

# CLEAR 
sll.clear()
```
</details>


#### [Doubly Linked List](/dsa_algos/doubly_linked_list.py)

<details>
<summary>Usage Example</summary>

```python
from dsa_algos.doubly_linked_list import DoublyLinkedList

# CREATE EMPTY LIST
dll = DoublyLinkedList()

# INSERT
dll.append(5)
dll.append(-5)
dll.prepend(10)
dll.prepend(100)
dll.insert(data=70, at_index=1)
dll.insert(data=100, at_index=-1)

# REMOVE
dll.pop()
dll.pop_first()
dll.remove(from_index=2)

# SEARCH 
dll.search('A')
dll.search('Z')

# SORT
dll.sort()

# PRINT
print(dll)

# CLEAR 
dll.clear()
```
</details>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.