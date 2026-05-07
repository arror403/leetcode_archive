class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        t=[]

        def inorderTraversal(root):
            if root is None: return
            inorderTraversal(root.left)
            t.append(root)
            inorderTraversal(root.right)

        def sortedArrayToBST(start, end):
            if (start > end): return None
            mid = (start + end) // 2
            root = t[mid]
            root.left = sortedArrayToBST(start, mid - 1)
            root.right = sortedArrayToBST(mid + 1, end)
            return root

        inorderTraversal(root)


        return sortedArrayToBST(0,len(t)-1)