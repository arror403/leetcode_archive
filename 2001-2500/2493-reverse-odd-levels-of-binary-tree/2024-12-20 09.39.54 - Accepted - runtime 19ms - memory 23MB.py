# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def traverse(node1, node2, lvl):
            if (node1==None or node2==None):
                return
            if lvl%2==1:
                node1.val, node2.val = node2.val , node1.val

            traverse(node1.left, node2.right, lvl + 1)
            traverse(node1.right, node2.left, lvl + 1)

        # We call the function from lvl 0, and everything starts from lvl 1
        traverse(root.left, root.right, 1)
        
        return root


# TC: O(n) -> Every node in the binary tree is visited
# SC: O(h) -> where h is the height of the binary tree