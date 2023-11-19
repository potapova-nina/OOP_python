class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None  

class RingList1:

    def __init__(self):
        self.head=None

    def add_list(self,data):
        if self.head==None:
            self.head=Node(data)
            self.head.next=self.head
        else:
            curr=self.head
            while curr.next!=self.head:
                curr=curr.next
            new_data=Node(data)
            curr.next=new_data
            curr=curr.next
            curr.next=self.head
    
    def display(self):
        iter_list=self.head
        print(iter_list.data, iter_list.next)
        while iter_list.next!=self.head:
            iter_list=iter_list.next
            print(iter_list.data, iter_list.next)

    def del_item(self,index):
        curr=self.head
        count=0
        while curr.next!=self.head:
            if count==index:
                break
            ref=curr
            curr=curr.next
            count+=1
        if curr==self.head:
            while curr.next!=self.head:
                curr=curr.next
            curr.next=self.head.next
            self.head=self.head.next
        else:
            if count!=index:
                print("Error")
            else:
                ref.next=curr.next
        
s=RingList1()
s.add_list(1)
s.add_list(2)
s.add_list(3)
s.add_list(4)

s.display()

s.del_item(0)
print("DONE")
s.display()


