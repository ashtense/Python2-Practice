from collections import deque

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data


class Solution:

    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        queue = deque()
        queue.append(root)
        while(len(queue)>0):
            node = queue.popleft()
            print(node.data, end =" ")

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)               
        

arrData = [3,5,4,7,2,1]
# arrData = [1]
myTree=Solution()
root=None
for i in arrData:
    data=int(i)
    root=myTree.insert(root,data)
myTree.levelOrder(root)