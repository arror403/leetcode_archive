class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        paths=self.allPaths(root)
        
        return sum(int(p, 2) for p in paths)


    def allPaths(self, node):
        if node:
            if not node.left and not node.right:
                yield str(node.val)
            else:
                yield from (str(node.val) + x for x in self.allPaths(node.left))
                yield from (str(node.val) + x for x in self.allPaths(node.right))