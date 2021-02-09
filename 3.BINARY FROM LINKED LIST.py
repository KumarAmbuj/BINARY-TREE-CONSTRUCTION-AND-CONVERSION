class LNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class BNode:
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

class Conversion:
    def __init__(self):
        self.head=None
        self.root=None

    def push(self,val):
        newnode=LNode(val)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def maketree(self):
        newnode=BNode(self.head.val)
        self.head=self.head.next
        if self.root==None:
            self.root=newnode
        queue=Queue()

        Enqueue(queue,self.root)

        while(Size(queue)):
            remnode=Dequeue(queue)

            lchild=None
            rchild=None
            if self.head!=None:
                lchild=BNode(self.head.val)
                self.head=self.head.next
                Enqueue(queue,lchild)

            if self.head:
                rchild=BNode(self.head.val)
                self.head=self.head.next
                Enqueue(queue,rchild)
            remnode.left=lchild
            remnode.right=rchild

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.val,end=' ')
            self.inorder(node.right)

conv = Conversion()
conv.push(36)
conv.push(30)
conv.push(25)
conv.push(15)
conv.push(12)
conv.push(10)

conv.maketree()
conv.inorder(conv.root)



