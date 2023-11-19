class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        pass
 
class RingClass2:
    def __init__(self):
        self.head=None
        pass
    def display(self):
        curr=self.head
        print(curr.prev,curr.data,curr.next)
        while curr.next!=self.head:
            curr=curr.next
            print(curr.prev,curr.data,curr.next)

    def add_list(self,data):
        if self.head==None:
            new_node=Node(data)
            self.head=new_node
            self.head.next=self.head.prev=self.head

        else:
            curr=self.head
            while curr.next!=self.head:
                curr=curr.next
            prev=curr
            new_node=Node(data)
            curr.next=new_node
            curr=curr.next
            curr.prev=prev
            curr.next=self.head
            self.head.prev=curr

    def del_item(self,index):
        curr=self.head
        count=0
        while curr.next!=self.head:
            if count==index:
                break
            count+=1
            curr=curr.next
        left=curr.prev
        right=curr.next
        left.next=right
        right.prev=left
        if curr==self.head:
            self.head=right


s=RingClass2()
s.add_list(1)
s.add_list(2)
s.add_list(3)
s.add_list(4)
s.add_list(5)

s.display()
s.del_item(4)
print("Done")
s.display()