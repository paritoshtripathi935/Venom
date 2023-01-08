"""
Doubly Linked List Conversion
Accuracy: 83.33% Submissions: 6 Points: 100
Given a doubly linked with each of the previous pointer assigned to null. Your task is to

assign previous pointer to each of previous nodes respectively.
Input Format :
First line of input contains number of testcases T. For each testcase, first line of input
contains length of linked list N and next line contains elements of linked list Lli].

Output Format :
For each testcase, print linked list in reverse order as per sample output shown below.
Task : Given all the other driver and utility functions. Your task is to complete function to
convert to doubly
Constraints :

1<=T<=100
1<=N<=100
0<=L[i]<=105
Example:
Input:
1
5
12345
Output:
5<-4<-3<-2<-1
"""

#User function Template for python3

def makeDoubly(head):
    #code here
    if head is None:
        return
    curr_node = head
    while curr_node.next is not None:
        curr_node.next.prev = curr_node
        curr_node = curr_node.next
    return

def Extra_Function(head):
    if head is None:
        return
    curr_node = head
    while curr_node.next is not None:
        curr_node = curr_node.next
    while curr_node.prev is not None:
        print(curr_node.data, end=" <- ")
        curr_node = curr_node.prev
    print(curr_node.data)
    return
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None
        self.prev= None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

def printList(head):
    if head is None:
        print(' ')
        return
    tail = head

    while(tail.next):
        tail=tail.next

    curr_node = tail
    while curr_node and curr_node.prev:
        print(curr_node.data, end=" <- ")
        curr_node = curr_node.prev
    print(head.data)
    return





if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        nodes = list(map(int,input().strip().split()))
        a = LinkedList()

        for node in nodes:
            a.append(node)
        makeDoubly(a.head)
        printList(a.head)
# } Driver Code Ends
        