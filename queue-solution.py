class Queue:
    def __init__(self):
        # TODO: Initialize the queue
        self.items = []

    def is_empty(self):
        # TODO: Implement the method
        return len(self.items)== 0

    def enqueue(self, item):
        # TODO: Implement the method
        self.items.append(item)

    def dequeue(self):
        # TODO: Implement the method
        if self.is_empty():
            raise IndexError("No items to dequeue")
        return self.items.pop()

    def peek(self):
        # TODO: Implement the method
        if self.is_empty():
            raise IndexError("No items to peek")
        return self.items[0]

    def size(self):
        # TODO: Implement the method
        return len(self.items)
    
queue = Queue()
print(queue.is_empty())  # Expected output: True

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.size())  # Expected output: 3

print(queue.dequeue())  # Expected output: 10
print(queue.peek())  # Expected output: 20
print(queue.size())  # Expected output: 2

original_queue = Queue()
original_queue.enqueue(10)
original_queue.enqueue(20)
original_queue.enqueue(30)

reversed_queue = reverse_queue(original_queue)

print(reversed_queue.dequeue())  # Expected output: 30
print(reversed_queue.dequeue())  # Expected output: 20
print(reversed_queue.dequeue()) 
