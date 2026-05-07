class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = []
        if root: q.append(root)

        while q:
            new_nodes = []
            for node in q: 
                if node and node.left: 
                    new_nodes.append(node.left)
                if node and node.right: 
                    new_nodes.append(node.right)
                    
            res.append([node.val for node in q])
            q = new_nodes


        return res 