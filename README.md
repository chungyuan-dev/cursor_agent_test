# cursor_agent_test

## Linked List Example

This repository contains a simple implementation of a singly linked list in Python.

### Files

- `linked_list_example.py` - Complete linked list implementation with examples

### Features

The linked list implementation includes:

- **Node Class**: Basic building block with data and next pointer
- **LinkedList Class**: Full implementation with the following operations:
  - `append(data)` - Add element to the end
  - `prepend(data)` - Add element to the beginning
  - `insert(index, data)` - Insert element at specific position
  - `delete(data)` - Remove first occurrence of data
  - `delete_at_index(index)` - Remove element at specific position
  - `find(data)` - Find index of element
  - `get(index)` - Get element at specific position
  - `is_empty()` - Check if list is empty
  - `length()` - Get number of elements
  - `display()` - Show visual representation
  - `reverse()` - Reverse the list in place

### Running the Example

```bash
python3 linked_list_example.py
```

### Example Output

The script demonstrates all linked list operations with clear output showing:
1. Creating and checking empty list
2. Adding elements (append/prepend)
3. Inserting at specific positions
4. Finding elements
5. Deleting elements
6. Reversing the list
7. Edge case handling

### Key Concepts Demonstrated

- **Node Structure**: Each node contains data and a reference to the next node
- **Dynamic Memory**: Nodes are created and linked dynamically
- **Traversal**: Walking through the list using the next pointers
- **Insertion/Deletion**: Manipulating pointers to add/remove nodes
- **Edge Cases**: Handling empty lists and single-element lists