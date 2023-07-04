class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Given a reference (pointer to pointer)
# to the head of a list and an int, inserts
# a new node on the front of the list.


def push(head_ref, new_data):
    # Create a new node
    new_node = Node(new_data)

    # Make the new node point to the current head
    new_node.next = head_ref

    # Update the head to point to the new node
    return new_node

# Given a reference (pointer to pointer)
# to the head of a list and an int,
# appends a new node at the end


def append(head_ref, new_data):
    # Create a new node
    new_node = Node(new_data)

    # Store the head reference in a temporary variable
    last = head_ref

    # Set the next pointer of the new node as None since it
    # will be the last node
    new_node.next = None

    # If the Linked List is empty, make the new node as the
    # head and return
    if head_ref is None:
        return new_node

    # Else traverse till the last node
    while last.next is not None:
        last = last.next

    # Change the next pointer of the last node to point to
    # the new node
    last.next = new_node

    return head_ref

# This function prints the contents of
# the linked list starting from the head


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next


# Driver code

    # Start with an empty list
head = None

# Insert nodes at the beginning of the linked list
head = push(head, 6)
head = push(head, 5)
head = push(head, 4)
head = push(head, 3)
head = push(head, 2)

print("Created Linked list is:")
printList(head)

    # Insert 1 at the end
head = append(head, 1)

print("\nAfter inserting 1 at the end:")
printList(head)