class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def search(inOrder,s,end,x):
    for i in range(s,end+1):
        if inOrder[i]==x:
            return i

def tree(inOrder,preOrder,s,end,c):
    if s>end:
        return None

    newnode=Node(preOrder[c[0]])
    c[0]+=1

    if s==end:
        return newnode

    index=search(inOrder,s,end,newnode.val)

    newnode.left=tree(inOrder,preOrder,s,index-1,c)
    newnode.right=tree(inOrder,preOrder,index+1,end,c)
    return newnode

def inorderprint(node):
    if node:
        inorderprint(node.left)
        print(node.val,end=' ')
        inorderprint(node.right)

def maketree(inorder,preorder):
    c=[0]
    node=tree(inorder,preorder,0,len(preorder)-1,c)
    inorderprint(node)
inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
maketree(inOrder,preOrder)



