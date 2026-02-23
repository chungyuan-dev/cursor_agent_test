# cursor_agent_test

## Doubly Linked List Example

This repository contains a simple implementation of a doubly linked list in Python.

### Files

- `linked_list_example.py` - Complete doubly linked list implementation with examples

### Features

The doubly linked list implementation includes:

- **Node Class**: Building block with data, a `next` pointer, and a `prev` pointer
- **LinkedList Class**: Full implementation with a `head` and `tail` pointer, supporting the following operations:
  - `append(data)` - Add element to the end (O(1))
  - `prepend(data)` - Add element to the beginning (O(1))
  - `insert(index, data)` - Insert element at specific position
  - `delete(data)` - Remove first occurrence of data
  - `delete_at_index(index)` - Remove element at specific position
  - `find(data)` - Find index of element
  - `get(index)` - Get element at specific position
  - `is_empty()` - Check if list is empty
  - `length()` - Get number of elements
  - `display()` - Show visual representation from head to tail (e.g. `None <-> 1 <-> 2 <-> None`)
  - `display_reverse()` - Show visual representation from tail to head
  - `reverse()` - Reverse the list in place

### Running the Example

```bash
python3 linked_list_example.py
```

### Example Output

The script demonstrates all doubly linked list operations with clear output showing:
1. Creating and checking empty list
2. Adding elements (append/prepend)
3. Inserting at specific positions
4. Finding elements
5. Deleting elements
6. Traversing in reverse (tail to head)
7. Reversing the list
8. Edge case handling

### Key Concepts Demonstrated

- **Node Structure**: Each node contains data and references to both the next and previous nodes
- **Bidirectional Traversal**: The list can be traversed in both directions using `next` and `prev` pointers
- **Tail Pointer**: A dedicated `tail` pointer enables O(1) append and reverse traversal
- **Insertion/Deletion**: Manipulating both `prev` and `next` pointers to add/remove nodes
- **Edge Cases**: Handling empty lists and single-element lists
