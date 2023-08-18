class binartTree:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
def insert(btreenode,val):
        if val<btreenode.val:
            if btreenode.left == None:
                btreenode.left=binartTree(val)
            else:
                insert(btreenode.left,val)
        else:
            if btreenode.right == None:
                btreenode.right=binartTree(val)
            else:
                insert(btreenode.right,val)
a = binartTree(100)
insert(a,10)
insert(a,20)
insert(a,30)
insert(a,0)
insert(a,1)
insert(a,110)
insert(a,100)
insert(a,710)
insert(a,290)
insert(a,190)

def inorderTraversal(node):
    if node.left!=None:
        inorderTraversal(node.left)
    print(node.val)
    if node.right!=None:
        inorderTraversal(node.right)
        
def preorderTraversal(node):
    print(node.val)
    if node.left!=None:
        preorderTraversal(node.left)
    
    if node.right!=None:
        preorderTraversal(node.right)

def postorderTraversal(node):
    if node.left!=None:
        postorderTraversal(node.left)
    if node.right!=None:
        postorderTraversal(node.right)
    print(node.val)
def bfs(node):
    if node == None:
        return []
    queue = [node]
    values = []
    while queue:
        current = queue.pop()
        print (current.val)
        values.append(current.val)
        if current.left!= None:
            queue.insert(0,current.left)
        if current.right != None:
            queue.insert(0,current.right)
    return values
bfs(a)
print("in order traversal")
inorderTraversal(a)
print(" pre order traversal")
preorderTraversal(a)
print(" post order traversal")
postorderTraversal(a)


