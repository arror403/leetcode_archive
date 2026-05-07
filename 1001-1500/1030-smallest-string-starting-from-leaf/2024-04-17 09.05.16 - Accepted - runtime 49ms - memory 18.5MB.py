# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def allPaths(node):
            if node:
                if not node.left and not node.right:
                    yield [node.val]
                else:
                    yield from ([node.val] + arr for arr in allPaths(node.left))
                    yield from ([node.val] + arr for arr in allPaths(node.right))

        p=allPaths(root)
        
        # print(list([[chr(i+97) for i in x] for x in p]))

        # t=list(map(lambda x:''.join(reversed(x)), [[chr(i+97) for i in x] for x in p]))


        return sorted(map(lambda x:''.join(reversed(x)), [[chr(i+97) for i in x] for x in p]))[0]