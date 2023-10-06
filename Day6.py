class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next 
mylist=Linkedlist()
first=node(10)
second=node(20)
third=node(30)
mylist.head=first
first.next=second
second.next=third
third.next=None
mylist.printlist()