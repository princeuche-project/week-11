# Introduction to Linked List

A Linked List is a data structure consisting of a sequence of nodes. Each node contains data and a reference (link) to the next node in the sequence. Or A linked list is a list in which the list items are linked to other list items in a specific way. Different forms of linked lists have different ways of linking objects.

## Linked List Operations

A Linked List typically supports the following operations:

- `insert(data)`: Inserts a new node with the given data at the beginning of the linked list.

 def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

- `delete(data)`: Deletes the node with the given data from the linked list.



- `search(data)`: Searches for a node with the given data in the linked list.

- `is_empty()`: Checks if the linked list is empty.

- `size()`: Returns the number of nodes in the linked list.


# Linked Lists Implementation
[Linkded List implementation](linked-list.py)

Click the link above to see the linked list implementation and examples
