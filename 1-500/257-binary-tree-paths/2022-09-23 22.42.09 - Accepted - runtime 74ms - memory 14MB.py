# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
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
            tmp=''
            for j in range(len(i)):
                tmp+=str(i[j])
                if j!=(len(i)-1): tmp+='->'
            res.append(tmp)
            
        return res