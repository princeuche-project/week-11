
"""


"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    """
    Nodes can either be appended or inserted at a specified position in this implementation.
    To append, we simply call the insert method and send the size of the list as the index.
    In the insert method, we first check if the specified index is valid or not, if not, we throw a ValueError.
    After passing the check, if the list is empty, we simply assign the new node to the head, increment the count, and return from the method.
    """
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    """
    To remove an item we must specify where the item is to be removed from. 
    If the specified index is out of range, we raise a ValueError.
    If there’s only one item on the list, we simply make the head None and the count 0, and return from the method.
    """

    def delete(self, data):
        current = self.head
        previous = None

        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next

    # Searches for a node with the given data in the linked list.
    def search(self, data):
        current = self.head

        while current:
            if current.data == data:
                return True
            current = current.next

        return False
    # Checks if the linked list is empty.
    def is_empty(self):
        return self.head is None
    
    #  Returns the number of nodes in the linked list.
    def size(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count
