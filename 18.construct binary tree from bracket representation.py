class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def Stack():
    s=[]
    return s
def Push(s,x):
    s.append(x)
def Pop(s):
    return s.pop()
def Size(s):
    return len(s)
def Top(s):
    return s[-1]
def findindex(sr,s,e):
    stack=Stack()
    for i in range(s,e+1):
        if sr[i]=='(':
            Push(stack,sr[i])
        elif sr[i]==')':

            x=Pop(stack)
            if Size(stack)==0:
                return i
    return -1
def maketree(sr,s,e):

    if s>e:
        return None

    node=Node(int(sr[s]))

    if s==e:
        return node

    index=-1
    if s+1<=e and sr[s+1]=='(':
        index=findindex(sr,s+1,e)
    if index!=-1:
        node.left = maketree(sr, s + 2, index - 1)
        node.right = maketree(sr, index + 2, e-1)

    return node

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=' ')
        inorder(node.right)


def construct(sr):
    node=maketree(sr,0,len(sr)-1)
    inorder(node)

sr = "4(2(3)(1))(6(5))"
construct(sr)
