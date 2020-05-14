#!usr/bin/python3

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None


class Link_list:
    def __init__(self):
        self.head=None


    def print_list(self):
        temp_node=self.head
        while temp_node:
            print(temp_node.data)
            temp_node=temp_node.next

    def list_length(self):
        temp_node=self.head
        length=0
        while temp_node:
            length+=1
            temp_node=temp_node.next
        return length

    def append(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return
        temp_node=self.head
        while temp_node.next:
            temp_node=temp_node.next
        temp_node.next=new_node

    def append_after(self,new_data,old_data):
        new_node=Node(new_data)
        temp_node=self.head

        while temp_node.next.data!=old_data:
            temp_node=temp_node.next
        new_node.next=temp_node.next.next
        temp_node.next.next=new_node

    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def delete_node(self,data):
        curr_node=self.head
        prev_node=self.head

        while curr_node.data!=data:
            prev_node=curr_node
            curr_node=curr_node.next
        prev_node.next=curr_node.next

    def swap(self,data1,data2):

        if data1==data2:
            print("both data are same and cannot perform swap on single node")
            return

        curr1=self.head
        prev1=None
        while curr1.data!=data1:
            prev1=curr1
            curr1=curr1.next

        curr2=self.head
        prev2=None
        while curr2.data!=data2:
            prev2=curr2
            curr2=curr2.next

        if curr1.data==self.head.data:
            curr1.next=curr2.next
            curr2.next=curr1
            self.head=curr2

        elif curr2.data==self.head.data:
            curr2.next=curr1.next
            curr1.next=curr2
            self.head=curr1

        else:
            prev1.next=curr2
            prev2.next=curr1
            curr1.next,curr2.next=curr2.next,curr1.next



llist=Link_list()
print("****append at last****")
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.print_list()
print("*****append after*****")
llist.append_after("E","C")#("new node","previous node dataafter which you want to insert ")
llist.print_list()
print("***prepend******")
llist.prepend("F")
llist.print_list()
print("******delete******")
llist.delete_node("E")
llist.print_list()
print("the length od link list is :"+str(llist.list_length()))

print("****swaping two nodes******* ")
llist.swap("F","C")
llist.print_list()
