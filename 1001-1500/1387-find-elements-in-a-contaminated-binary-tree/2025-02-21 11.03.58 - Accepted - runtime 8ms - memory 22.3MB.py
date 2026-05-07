class FindElements:

    def __init__(self, root: TreeNode):
        self.seen = set()
        
        def dfs(node: TreeNode, v: int):
            if node:
                node.val=v
                self.seen.add(v)
                dfs(node.left, 2*v+1)
                dfs(node.right, 2*v+2)
            
        dfs(root, 0)
        
        
    def find(self, target: int) -> bool:
        return target in self.seen