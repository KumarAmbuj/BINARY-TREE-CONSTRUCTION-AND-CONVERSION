class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def maketree(arr,s,e):
    if s>e:
        return None

    mx=arr[s]
    index=s
    for i in range(s+1,e+1):
        if arr[i]>mx:
            mx=arr[i]
            index=i

    newnode=Node(arr[index])
    if s==e:
        return newnode
    newnode.left=maketree(arr,s,index-1)
    newnode.right=maketree(arr,index+1,e)

    return newnode
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=' ')
        inorder(node.right)

def construct(arr):
    node=maketree(arr,0,len(arr)-1)
    inorder(node)



arr = [5, 10, 40, 30, 28]
construct(arr)