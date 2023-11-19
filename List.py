class DoublyNode:

    def __init__(self,data=None,next=None, prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class DoublyList:

    def __init__(self): #constructor
        self.head=None
        self.tail=None

    def add_to_DoublyList(self,data):
        if self.head==None:
            self.head=DoublyNode(data)
            self.tail=self.head
            return
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            new_node=DoublyNode(data)
            curr.next=new_node
            ref=curr
            curr=curr.next
            curr.prev=ref
            self.tail=curr

    def delete_node(self,index):
        curr=self.head
        count=0
        while curr!=None:
            if count==index:
                break
            count+=1
            curr=curr.next

        left=curr.prev
        right=curr.next

        if right!=None:
            right.prev=left
        if left!=None:
            left.next=right
        
        if curr==self.head:
            self.head=right
        if curr==self.tail:
            self.tail=left



    def display(self):
        iter_list=self.head
        while iter_list!=None:
            print(iter_list.prev, iter_list.data, iter_list.next)
            iter_list=iter_list.next


d_lis=DoublyList()
d_lis.add_to_DoublyList(1)
d_lis.add_to_DoublyList(2)
d_lis.add_to_DoublyList(3)
d_lis.add_to_DoublyList(4)
d_lis.add_to_DoublyList(5)

# d_lis.delete_node(1)

d_lis.display()


print("DONE")
d_lis.delete_node(0)
d_lis.display()
