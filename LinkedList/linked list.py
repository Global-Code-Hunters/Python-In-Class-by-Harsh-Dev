
class Node:
    def __init__(self,data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data
    def set_data(self,data):
        self.__data=data
    def get_next(self):
        return self.__next
    def set_next(self,next_node):
        self.__next=next_node

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    def get_head(self):
        return self.__head
    def get_tail(self):
        return self.__tail
    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node
    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data(),end='->')
            temp=temp.get_next()

ll=LinkedList()
ll.add(30)
ll.add(40)
ll.add(50)
ll.add(60)
ll.display()
print("None")



'''
OUTPUT

30->40->50->60->None

'''
