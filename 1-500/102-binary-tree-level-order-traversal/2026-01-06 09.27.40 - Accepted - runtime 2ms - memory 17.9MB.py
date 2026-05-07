class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, level = [], [root]

        while level:
            res.append([node.val for node in level])
            tmp = []

            for node in level:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
                
            level = tmp


        return res