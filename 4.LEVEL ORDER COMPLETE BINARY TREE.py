class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def maketree(arr,i,n):
    if i<n:
        newnode = Node(arr[i])

        newnode.left=maketree(arr, 2 * i + 1, n)
        newnode.right=maketree(arr,2*i+2,n)
        return newnode

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=' ')
        inorder(node.right)


arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
root=maketree(arr,0,len(arr))
inorder(root)
