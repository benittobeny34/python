class Node:
    def __init__(self,data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

def make_bst(arr):
    if not arr:
        return None

    mid = len(arr)//2

    root = Node(arr[mid])
    root.left = make_bst(arr[:mid])
    root.right = make_bst(arr[mid+1:])

    return root
    

arr = [2,3,4,5,6,7,8]

head = make_bst(arr)
print(head.data)
print(head.left.data)
print(head.left.right.data)
print(head.left.left.data)

print(head.right.data)
print(head.right.left.data)
print(head.right.right.data)

