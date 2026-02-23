from typing import Optional, Any

class Node:
    """A node in a doubly linked list containing data and references to the next and previous nodes."""

    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['Node'] = None
        self.prev: Optional['Node'] = None

class LinkedList:
    """A simple implementation of a doubly linked list."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        """Add a new node with the given data to the end of the list."""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def prepend(self, data):
        """Add a new node with the given data to the beginning of the list."""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def insert(self, index, data):
        """Insert a new node with the given data at the specified index."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(data)
            return

        if index == self.size:
            self.append(data)
            return

        new_node = Node(data)
        current = self.head

        for i in range(index - 1):
            current = current.next

        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        self.size += 1

    def delete(self, data):
        """Delete the first occurrence of the given data from the list."""
        current = self.head

        while current:
            if current.data == data:
                self._unlink(current)
                return True
            current = current.next

        return False

    def delete_at_index(self, index):
        """Delete the node at the specified index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        current = self.head
        for i in range(index):
            current = current.next

        self._unlink(current)

    def _unlink(self, node):
        """Remove a node from the list by updating its neighbours' pointers."""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        self.size -= 1

    def find(self, data):
        """Find the index of the first occurrence of the given data."""
        current = self.head
        index = 0

        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1

        return -1  # Not found

    def get(self, index):
        """Get the data at the specified index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        current = self.head
        for i in range(index):
            current = current.next

        return current.data

    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None

    def length(self):
        """Get the number of nodes in the list."""
        return self.size

    def display(self):
        """Return a string representation of the list from head to tail."""
        if not self.head:
            return "Empty list"

        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next

        return "None <-> " + " <-> ".join(elements) + " <-> None"

    def display_reverse(self):
        """Return a string representation of the list from tail to head."""
        if not self.tail:
            return "Empty list"

        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev

        return "None <-> " + " <-> ".join(elements) + " <-> None"

    def reverse(self):
        """Reverse the doubly linked list in place."""
        current = self.head

        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev  # Move to the next node (now stored in prev)

        self.head, self.tail = self.tail, self.head


def main():
    """Demonstrate the doubly linked list operations with examples."""
    print("=== Doubly Linked List Example ===\n")

    # Create a new linked list
    ll = LinkedList()

    print("1. Creating an empty doubly linked list:")
    print(f"   List: {ll.display()}")
    print(f"   Is empty: {ll.is_empty()}")
    print(f"   Length: {ll.length()}\n")

    # Add elements to the list
    print("2. Adding elements:")
    ll.append(10)
    print(f"   After appending 10: {ll.display()}")

    ll.append(20)
    ll.append(30)
    print(f"   After appending 20, 30: {ll.display()}")

    ll.prepend(5)
    print(f"   After prepending 5: {ll.display()}")
    print(f"   Length: {ll.length()}\n")

    # Insert at specific position
    print("3. Inserting at specific positions:")
    ll.insert(2, 15)
    print(f"   After inserting 15 at index 2: {ll.display()}")

    ll.insert(0, 1)
    print(f"   After inserting 1 at index 0: {ll.display()}\n")

    # Find elements
    print("4. Finding elements:")
    print(f"   Index of 15: {ll.find(15)}")
    print(f"   Index of 100 (not in list): {ll.find(100)}")
    print(f"   Element at index 3: {ll.get(3)}\n")

    # Delete elements
    print("5. Deleting elements:")
    print(f"   Before deletion: {ll.display()}")

    ll.delete(15)
    print(f"   After deleting 15: {ll.display()}")

    ll.delete_at_index(0)
    print(f"   After deleting element at index 0: {ll.display()}")
    print(f"   Length: {ll.length()}\n")

    # Traverse in reverse using display_reverse
    print("6. Traversing in reverse (tail to head):")
    print(f"   Forward:  {ll.display()}")
    print(f"   Backward: {ll.display_reverse()}\n")

    # Reverse the list
    print("7. Reversing the list:")
    print(f"   Before reverse: {ll.display()}")
    ll.reverse()
    print(f"   After reverse: {ll.display()}\n")

    # Edge cases
    print("8. Testing edge cases:")
    empty_list = LinkedList()
    print(f"   Empty list: {empty_list.display()}")
    print(f"   Deleting from empty list: {empty_list.delete(10)}")

    single_item_list = LinkedList()
    single_item_list.append(42)
    print(f"   Single item list: {single_item_list.display()}")
    single_item_list.reverse()
    print(f"   Reversed single item list: {single_item_list.display()}")


if __name__ == "__main__":
    main()
