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
    def findmin(self):
        if self.root == None:
            return "Tree is empty"
        else:
            return self._findmin(self.root)
    def _findmin(self,root):
        if root.left == None:
            return root.data
        else:
            return self._findmin(root.left)
        
    def findmax(self):
        if self.root ==None:
            return "TRee is empty"
        else:
            return self._findmax(self.root)
    def _findmax(self,root):
        if root.right == None:
            return root.data
        else:
            return self._findmax(root.right)
    def sumbst(self):
        if self.root == None:
            return "Tree is empty"
        else:
            return self._sum(self.root)
    def _sum(self,root):
        leftsum = rightsum = 0
        if root.left != None:           
            leftsum = self._sum(root.left)
        if root.right != None:         
            rightsum = self._sum(root.right)
        return root.data +leftsum + rightsum

bst = BST()

for  i in range(20,30,2):
    bst.insert(i)
for i in range(10,30,3):
    bst.insert(i)

print('inserted')
print('minimum value in the tree:',bst.findmin())
print('maximum value in the tree:',bst.findmax())

print('Sum of all elements in the tree:',bst.sumbst())
print('*'*15)
print('program exected succesfully')
