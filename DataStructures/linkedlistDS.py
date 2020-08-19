class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next;
class LinkedList:
    def __init__(self):
        self.head = None
        
    def _insert(self,data):
        if self.head == None:
           self.head = Node(data)
        else:
            self.insert(data,self.head)
    def insert(self,data,node):
        if node.next == None:
            node.next = Node(data)
        else:
            self.insert(data,node.next)





head = LinkedList()


for i in range(10):
    head._insert(i)

temp = head.head
while(temp):
    print(temp.data)
    temp = temp.next
