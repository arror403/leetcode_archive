# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:     
        if depth==1:
            # Store the node having the value val
            t=TreeNode(val)
            # Join node t with the root node
            t.left=root
            return t
  

        # Stores the current Level
        currLevel = 1
        # For performing BFS traversal
        Q=deque()
        # Add root node to Queue Q
        Q.append(root)
  

        while Q and currLevel<depth-1:
            # Stores the count of the total nodes at the currLevel
            l=len(Q)
  
            while l>0:
                node=Q[0]
                Q.popleft()
  
                if node.left:
                    Q.append(node.left)
  
                if node.right:
                    Q.append(node.right)
  
                l-=1
  
            currLevel+=1
  
        while Q:
            temp=Q[0]
            Q.popleft()

            temp1=temp.left
            temp.left=TreeNode(val)
            temp.left.left=temp1

            temp2=temp.right
            temp.right=TreeNode(val)
            temp.right.right=temp2
  
        return root