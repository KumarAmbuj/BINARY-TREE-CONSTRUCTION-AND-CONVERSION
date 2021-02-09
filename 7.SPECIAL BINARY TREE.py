class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def maketree(pre,preln,c):

    newnode=Node(pre[c[0]])
    c[0]+=1

    if preln[c[0]-1]=='L':
        return newnode

    newnode.left=maketree(pre,preln,c)
    newnode.right=maketree(pre,preln,c)

    return newnode

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=' ')
        inorder(node.right)


def construct(pre,preln):
    c=[0]
    node=maketree(pre,preln,c)
    inorder(node)

pre = [10, 30, 20, 5, 15]
preLN = ['N', 'N', 'L', 'L', 'L']
construct(pre,preLN)