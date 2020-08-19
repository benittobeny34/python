class Node:
    def __init__(self,data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

        
class BST:
    def __init__(self):
        self.root = None
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

            
    def _insert(self,data,root):      
        if data < root.data:
            if root.left == None:
                root.left = Node(data)
            else:
                self._insert(data,root.left)
        else:
            if root.right == None:
                root.right = Node(data)
            else:
                self._insert(data,root.right)
    def find(self,data):
        if self.root == None:
            return False
        else:
            return self._find(data,self.root)
            
    def _find(self,data,root):
        if root == None:
            return False
        if data == root.data:
            return True
        elif data < root.data:
            return self._find(data,root.left)
        else:  
            return self._find(data,root.right)

        
    def floor_ceil(self,data):
        if self.root == None:
            return None,None
        else:
           return  self._floor_ceil(self.root,data)
        
    def _floor_ceil(self,root,data,floor=None,ceil=None):
        #print('floor value:',floor,'ceil value:',ceil,'')
        if root == None:
            return floor,ceil
        if root.data == data:
            return data,data
        elif data < root.data:
            floor,ceil = self._floor_ceil(root.left,data,floor,root.data)
        elif data > root.data:
            floor,ceil = self._floor_ceil(root.right,data,root.data,ceil)

        return floor,ceil
        
        
            


head = BST()

for i in range(0,100,3):
    head.insert(i)
for i in range(0,100,4):
    print(i,'is present:',head.find(i))
for i in range(0,100,2):
    floor,ceil= head.floor_ceil(i)
    print('the floor value is of ',i,'is:',floor,'and the ceil is:',ceil)
    
    
