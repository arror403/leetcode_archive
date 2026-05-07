# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], K: int, L: int) -> Optional[TreeNode]:     
    # If L is 1
        if (L == 1):
  
            # Store the node having
            # the value K
            t = TreeNode(K)
  
            # Join node t with the
            # root node
            t.left = root
            return t
  
        # Stores the current Level
        currLevel = 1
  
        # For performing BFS traversal
        Q =[]
             
        # Add root node to Queue Q
        Q.append(root)
  
        # Traversal while currLevel
        # is less than L - 1
        while (len(Q)!=0 and currLevel < L - 1):
  
            # Stores the count of the
            # total nodes at the
            # currLevel
            Len = len(Q)
  
            # Iterate while len
            # is greater than 0
            while (Len > 0):
  
                # Pop the front
                # element of Q
                node = Q[0]
                Q = Q[1:]
  
                # If node.left is
                # not None
                if (node.left != None):
                    Q.append(node.left)
  
                # If node.right is
                # not None
                if (node.right != None):
                    Q.append(node.right)
  
                # Decrement len by 1
                Len -= 1
  
            # Increment currLevel by 1
            currLevel += 1
  
        # Iterate while Q is
        # non empty()
        while (len(Q)!=0):
  
            # Stores the front node
            # of the Q queue
            temp = Q[0]
            Q = Q[1:]
  
            # Stores its left sub-tree
            temp1 = temp.left
  
            # Create a Node with
            # value K and assign to
            # temp.left
            temp.left = TreeNode(K)
  
            # Assign temp1 to the
            # temp.left.left
            temp.left.left = temp1
  
            # Store its right subtree
            temp2 = temp.right
  
            # Create a Node with
            # value K and assign to
            # temp.right
            temp.right = TreeNode(K)
  
            # Assign temp2 to the
            # temp.right.right
            temp.right.right = temp2
  
        # Return the updated root
        return root