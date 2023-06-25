class MyQueue():
    # Using Python Lists as a Queue
    def __init__(self):
        self.queue = []
 
    def enqueue(self, value):
        # Inserting to the end of the queue
        self.queue.append(value)
 
    def dequeue(self):
         # Remove the furthest element from the top,
         # since the Queue is a FIFO structure
         return self.queue.pop(0)
    
    def size(self):
        if len( self.queue) > 0:
        

           return self.queue
 
 
my_q = MyQueue()
 
my_q.enqueue("Christopher")
my_q.enqueue("John")
my_q.enqueue("Michael")
my_q.enqueue("Uchenna")
 
for i in my_q.queue:
    print(i)
 
print('Popped,', my_q.dequeue())
print('Popped,', my_q.dequeue())
 
for i in my_q.queue:
    print(i)

print("total:", my_q.size())