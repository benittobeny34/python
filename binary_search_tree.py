class Node:
    def __init__(self,data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right;
        print(data)
        
class BST:
    def __init__(self):
        self.root = None

    def insert(self,x):
        if self.root == None:
            self.root = Node(x)
            
        else:
            self._insert(x,self.root)
    def _insert(self,data,root):
        if data < root.data:
            if root.left == None:
                root.left = Node(data)
            else:
                self._insert(data,root.left)
        else:
            if root.right ==None:
                root.right = Node(data)
            else:
                return self._insert(data,root.right)

    def find(self,value):
        if self.root == None:
            return False
        else:
            return self._find(value,self.root)
    def _find(self,value,root):
        if root == None:
            return False
        elif root.data == value:
            return True
        elif root.data < value:
            return self._find(value,root.left)
        else:
            return self._find(value,root.right)



head = BST();
print(head.root)


head.insert(5)
head.insert(7)
head.insert(8)
head.insert(9)

print(head.find(5))
print(head.find(11))
