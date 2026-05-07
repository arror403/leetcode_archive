# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # function for constructing trees
        def constructTrees(start, end):
        
            list = []
        
            """ if start > end then subtree will be
                empty so returning None in the list """
            if (start > end) :
            
                list.append(None)
                return list
            
            """ iterating through all values from
                start to end for constructing
                left and right subtree recursively """
            for i in range(start, end + 1):
            
                """ constructing left subtree """
                leftSubtree = constructTrees(start, i - 1)
        
                """ constructing right subtree """
                rightSubtree = constructTrees(i + 1, end)
        
                """ now looping through all left and
                    right subtrees and connecting
                    them to ith root below """
                for j in range(len(leftSubtree)) :
                    left = leftSubtree[j]
                    for k in range(len(rightSubtree)):
                        right = rightSubtree[k]
                        node = TreeNode(i)   # making value i as root
                        node.left = left    # connect left subtree
                        node.right = right    # connect right subtree
                        list.append(node)    # add this tree to list
            return list
        return constructTrees(1,n)