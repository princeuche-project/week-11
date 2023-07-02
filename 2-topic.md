# Introduction to Linked List

A Linked List is a data structure consisting of a sequence of nodes. Each node contains data and a reference (link) to the next node in the sequence. Or A linked list is a list in which the list items are linked to other list items in a specific way. Different forms of linked lists have different ways of linking objects.

The linked list or one way list is a linear set of data elements which is also termed as nodes. Here, the linear order is specified using pointers.

Each node is separated into two different parts:

The first part holds the information of the element or node
The second piece contains the address of the next node (link / next-pointer field) in this structure list.



![Alt text](image.png)



Linked lists can be measured as a form of high-level standpoint as being a series of nodes where each node has at least one single pointer to the next connected node, and in the case of the last node, a null pointer is used for representing that there will be no further nodes in the linked list. In the data structure, you will be implementing the linked lists which always maintain head and tail pointers for inserting values at either the head or tail of the list is a constant time operation. Randomly inserting of values is excluded using this concept and will follow a linear operation. As such, linked lists in data structure have some characteristics which are mentioned below:

* Insertion is O(1)

* Deletion is O(n)

* Searching is O(n)

Linked lists have a few key points that usually make them very efficient for implementing. These are:

* The list is dynamic and hence can be resized based on the requirement
* Secondly, the insertion is O(1).