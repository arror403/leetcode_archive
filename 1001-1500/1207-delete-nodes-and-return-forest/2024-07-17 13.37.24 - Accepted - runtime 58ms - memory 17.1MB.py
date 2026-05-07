class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        def helper(node, result, to_delete, is_root):
            if node is None: return None

            deleted = node.val in to_delete

            if (is_root and not deleted): result.append(node)

            node.left = helper(node.left, result, to_delete, deleted)
            node.right = helper(node.right, result, to_delete, deleted)

            return None if deleted else node


        result=[]
        helper(root, result, to_delete, True)

        return result