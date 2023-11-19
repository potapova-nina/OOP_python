class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    
    def enqueue(self,data):
        if self.front==None:
            new_node=Node(data)
            self.rear=self.front=new_node
        else:
            curr=self.rear
            new_node=Node(data)
            self.rear=new_node
            self.rear.next=curr

    def display(self):
        if self.rear==None:
            return
        curr=self.rear
        print(curr.data,curr.next)
        while curr.next!=None:
            curr=curr.next
            print(curr.data,curr.next)

    def dequeue(self):
        if self.rear==None:
            return
        
        curr=self.rear
        while curr.next!=self.front:
            curr=curr.next
        curr.next=None
        self.front=curr

q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.display()
q.dequeue()


print("DONE")
q.display()