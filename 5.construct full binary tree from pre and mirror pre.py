class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def search(x,prem,s,e):
    for i in range(s,e+1):
        if prem[i]==x:
            return i
def maketree(pre,prem,c,s,e):

    if s>e:
        return None

    newnode=Node(pre[c[0]])
    c[0]+=1

    if s==e:
        return newnode
    index=search(pre[c[0]],prem,s,e)

    newnode.left=maketree(pre,prem,c,index,e)
    newnode.right=maketree(pre,prem,c,s+1,index-1)

    return newnode

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=' ')
        inorder(node.right)




def construct(pre,prem):
    c=[0]
    node=maketree(pre,prem,c,0,len(pre)-1)
    inorder(node)


pre = [1, 2, 4, 5, 3, 6, 7]
prem = [1, 3, 7, 6, 2, 5, 4]
construct(pre,prem)