"""

 Created by akiselev on 2019-05-28
 
 
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        if not head:
            return Node(data)
        elif not head.next:
            head.next = Node(data)
        else:
            self.insert(head.next,data)
        return head


    #Complete this method


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);