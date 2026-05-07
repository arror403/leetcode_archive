# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def allPaths(node):
            if node:
                if not node.left and not node.right: # Leaf
                    yield [node.val]
                else:
                    yield from ([node.val] + arr for arr in allPaths(node.left))
                    yield from ([node.val] + arr for arr in allPaths(node.right))
        m=allPaths(root)
        res=[]
        for i in m:
            if sum(i)==targetSum:
                res.append(i) 
                
        return res