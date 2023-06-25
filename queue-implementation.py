class Queue:
# Let's  use python lists as a queue
    def __init__(self):
        self.items = []
# Check to see if the queue is empty

    def is_empty(self):
        return len(self.items) == 0
# To add a new item to the rear queue

    def enqueue(self, item):
        self.items.append(item)
# To remove item from the queue

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
# To check the size of the queue

    def size(self):
        return len(self.items)
#  Returns the item at the front of the queue without removing it.

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]


# my_q = Queue()
# my_q.enqueue(8)
# my_q.enqueue(10)
# my_q.enqueue(11)
# my_q.enqueue(14)

# print(my_q)
