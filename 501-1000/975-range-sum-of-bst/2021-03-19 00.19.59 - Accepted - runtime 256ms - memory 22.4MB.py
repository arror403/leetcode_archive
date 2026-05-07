# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    b=0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sum=0
        b=self.inorderTraversal(root)
        for i in b:
            if (i>=low)&(i<=high):
                sum+=i
        return sum
            
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root: TreeNode, res: List[int]) -> None:
        if not root: return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)
    