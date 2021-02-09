class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def Queue():
    queue=[]
    return queue
def Enqueue(q,s):
    q.append(s)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=' ')
        inorder(node.right)
def construct(arr):

    queue=Queue()
    index=0
    for i in range(len(arr)):
        if arr[i]==-1:
            index=i

    newnode=Node(index)
    root=newnode

    Enqueue(queue,newnode)

    while(Size(queue)):
        rem=Dequeue(queue)

        val=rem.val
        index=-1
        for i in range(len(arr)):
            if arr[i]==val:
                index=i
                arr[i]=-1
                break
        if index!=-1:
            newnode=Node(index)
            rem.left = newnode
            Enqueue(queue,newnode)

        val = rem.val
        index = -1
        for i in range(len(arr)):
            if arr[i] == val:
                index = i
                arr[i] = -1
                break
        if index != -1:
            newnode = Node(index)
            rem.right = newnode
            Enqueue(queue, newnode)
    inorder(root)

parent = [-1, 0, 0, 1, 1, 3, 5]
construct(parent)


