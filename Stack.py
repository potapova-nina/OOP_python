class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
    
    def push(self,data):
        if self.top==None:
            new_node=Node(data)
            self.top=new_node
        else:
            new_node=Node(data)
            curr=self.top
            self.top=new_node
            self.top.next=curr

    def display(self):
        if self.top==None:
            return 
        else:
            curr=self.top
            print(curr.data,curr.next)
            while curr.next!=None:
                curr=curr.next
                print(curr.data,curr.next)
        

    def pop(self):
        if self.top==None:
            return
        else:
            self.top=self.top.next
        # print(self.top)


s=Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)

s.display()
s.pop()

print("DONE")

s.display()