from typing import Optional, Any

class Node:
    """A node in a linked list containing data and a reference to the next node."""
    
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['Node'] = None

class LinkedList:
    """A simple implementation of a singly linked list."""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data):
        """Add a new node with the given data to the end of the list."""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def prepend(self, data):
        """Add a new node with the given data to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert(self, index, data):
        """Insert a new node with the given data at the specified index."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.prepend(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        for i in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete(self, data):
        """Delete the first occurrence of the given data from the list."""
        if not self.head:
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def delete_at_index(self, index):
        """Delete the node at the specified index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        if index == 0 and self.head:
            self.head = self.head.next
            self.size -= 1
            return
        
        current = self.head
        for i in range(index - 1):
            if current:
                current = current.next
        
        if current and current.next:
            current.next = current.next.next
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
            if current:
                current = current.next
        
        if current:
            return current.data
        raise IndexError("Index out of range")
    
    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None
    
    def length(self):
        """Get the number of nodes in the list."""
        return self.size
    
    def display(self):
        """Return a string representation of the list."""
        if not self.head:
            return "Empty list"
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        return " -> ".join(elements) + " -> None"
    
    def reverse(self):
        """Reverse the linked list in place."""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev


def main():
    """Demonstrate the linked list operations with examples."""
    print("=== Linked List Example ===\n")
    
    # Create a new linked list
    ll = LinkedList()
    
    print("1. Creating an empty linked list:")
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
    
    # Reverse the list
    print("6. Reversing the list:")
    print(f"   Before reverse: {ll.display()}")
    ll.reverse()
    print(f"   After reverse: {ll.display()}\n")
    
    # Edge cases
    print("7. Testing edge cases:")
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