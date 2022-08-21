## DSA ALGORITHMS 

BELOW TOPICS ARE COVERED ALONG WITH USAGE (Scroll to see) 

- SEARCHING ([Linear, Binary Search](/dsa_algos/search.py))
- SORTING ([Merge Sort](/dsa_algos/sort.py))
- LINKED LIST ([Singly Linked List](/dsa_algos/singly_linked_list.py), [Doubly Linked List](/dsa_algos/doubly_linked_list.py))
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

### **SEARCHING**

<details>
<summary>Example</summary>

```python
from dsa_algos.search import SearchAlgo

print(SearchAlgo.linear_search([1,2,3,4,5], 4))
print(SearchAlgo.linear_search_all_elements([1,2,3,4,5,5,5,6,7], 4))
print(SearchAlgo.binary_search(['a', 'A', 'b', 'B'], 'A'))
```
</details>

### **SORTING**

<details>
<summary>Example</summary>

```python
from dsa_algos.sort import SortAlgo
print(SearchAlgo.merge_sort([1,2,3,4,5], 4))
```
</details>

### **LINKED LIST**
#### **Singly Linked List**

<details>
<summary>Example</summary>

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


#### **Doubly Linked List**

<details>
<summary>Example</summary>

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