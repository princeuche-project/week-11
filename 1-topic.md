# Introduction To Queue

Welcome to the Queue tutorial! In this module, we will explore the Queue data structure and its implementation in Python. A queue is an ordered collection of elements that follows the First-In-First-Out (FIFO) principle, meaning that the element inserted first will be the first one to be removed.
Before we dive into the details, let's cover the basics of the Queue data structure, its purpose, performance, and common use cases.

## Purpose os Queue
The primary purpose of a Queue data structure is to efficiently manage a collection of elements in a way that allows adding elements at one end (rear) and removing elements from the other end (front). It follows the FIFO principle, which makes it suitable for scenarios where the order of elements is crucial.
Queues are commonly used in various applications, such as:

* Task scheduling: Queues can be used to prioritize tasks or processes based on their arrival time or priority levels.

* Breadth-first search: Queues are used in graph algorithms like breadth-first search (BFS) to explore nodes level by level.

* Print spooling: A queue can be used to manage print jobs, ensuring they are processed in the order they were submitted.

### Performance of Queues
The performance of a Queue data structure can be analyzed using Big O notation, which provides an estimation of the algorithmic complexity in terms of time and space.
Here are the time complexities for common operations on a Queue:

* Enqueue: Adding an element to the rear of the queue takes O(1) time as it involves updating a reference to the last element.

* Dequeue: Removing an element from the front of the queue also takes O(1) time since we maintain a reference to the first element.

* Peek: Accessing the element at the front of the queue (without removing it) is an O(1) operation.

It's important to note that these time complexities assume the underlying data structure used to implement the queue (e.g., an array or linked list) provides efficient insertion and deletion at both ends.
The space complexity of a Queue is determined by the number of elements stored in it. In the best case, the space complexity is O(1) when the queue is empty, and in the worst case, it is O(n) when n elements are present in the queue.

### Queue Implementation
In Python, we can implement a Queue using different underlying data structures. One common approach is to use a Python list as the underlying container, where the front of the queue corresponds to the list's beginning, and the rear corresponds to its end.

Click the below link to see the code example

[Queue implementation](queue-implementation.py)

## Explanation:
In this implementation, the Queue class utilizes a list (self.items) to store the elements. The is_empty method checks whether the queue is empty by verifying the length of the list.
The enqueue method adds an element to the rear of the queue using the append method of the list.
The dequeue method removes and returns the element at the front of the queue using the pop(0) method, which removes the first element from the list.
The peek method returns the element at the front of the queue without removing it.
The size method returns the current number of elements in the queue.

### Common Errors and Challenges
While working with queues, you may encounter some common errors and challenges. Here are a few to be aware of:
* IndexError: This error occurs when attempting to dequeue or peek an element from an empty queue. To avoid this, always check if the queue is empty before performing these operations.
* Forgetting to enqueue: It's important to ensure that all elements that need to be processed are properly enqueued. Failing to enqueue an element may lead to incorrect results or unexpected behavior in the algorithm or application utilizing the queue.
It's crucial to test your code thoroughly and handle these potential errors to ensure the correctness and reliability of your programs.

## Problem: Implementing a Queue
Now, let's solve a problem together to solidify your understanding of the Queue data structure. Your task is to implement a Queue using a Python list as the underlying container.
Write a Python class named Queue that supports the following methods:
* is_empty(): Returns True if the queue is empty, False otherwise.
* enqueue(item): Adds the given item to the rear of the queue.
* dequeue(): Removes and returns the item at the front of the queue. If the queue is empty, raise an IndexError with the message "Queue is empty."
* peek(): Returns the item at the front of the queue without removing it. If the queue is empty, raise an IndexError with the message "Queue is empty."
* size(): Returns the current number of elements in the queue.

## Work on the below Queue class

class Queue:

    def __init__(self):
        # TODO: Initialize the queue
    
    def is_empty(self):
        # TODO: Implement the method
    
    def enqueue(self, item):
        # TODO: Implement the method
    
    def dequeue(self):
        # TODO: Implement the method
    
    def peek(self):
        # TODO: Implement the method
    
    def size(self):
        # TODO: Implement the method

Once you have implemented the Queue class, you can test it with the following code:

queue = Queue()
print(queue.is_empty())  # Expected output: True

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.size())  # Expected output: 3

print(queue.dequeue())  # Expected output: 10
print(queue.peek())  # Expected output: 20
print(queue.size())  # Expected output: 2




[Queue Solution](queue-solution.py)

### Conclusion
Congratulations on completing the Queue tutorial! You have learned about the purpose and performance of the Queue data structure, its implementation in Python, and common errors and challenges associated with it. You have also solved two problems, including implementing a Queue and reversing a Queue.
By mastering the Queue data structure, you are equipped with a valuable tool for solving various programming problems efficiently.
