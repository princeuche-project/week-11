class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def size(self):
        return len(self.items)

# my_q = Queue()
# my_q.enqueue(8)
# my_q.enqueue(10)
# my_q.enqueue(11)
# my_q.enqueue(14)

# print(my_q)
