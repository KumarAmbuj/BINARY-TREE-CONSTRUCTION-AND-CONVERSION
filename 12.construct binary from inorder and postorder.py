class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def maketree(inorder,posorder,c,s,e):

    if s>e:
        return None

    newnode=Node(posorder[c[0]])
    c[0]-=1

    if s==e:
        return newnode

    index=-1
    for i in range(s,e+1):
        if inorder[i]==newnode.val:
            index=i
            break
    newnode.right = maketree(inorder, posorder, c, index + 1, e)
    newnode.left=maketree(inorder,posorder,c,s,index-1)

    return newnode

def printinorder(node):
    if node:
        printinorder(node.left)
        print(node.val,end=' ')
        printinorder(node.right)

def construct(inorder,posorder):
    c=[len(inorder)-1]
    node=maketree(inorder,posorder,c,0,len(inorder)-1)
    printinorder(node)

In = [4, 8, 2, 5, 1, 6, 3, 7]
pos = [8, 4, 5, 2, 6, 7, 3, 1]
construct(In,pos)