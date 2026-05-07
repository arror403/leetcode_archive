class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(head: ListNode, root: TreeNode) -> bool:
            if not head:
                return True
            if not root:
                return False
            if root.val != head.val:
                return False
            return dfs(head.next, root.left) or dfs(head.next, root.right)


        def search(head: ListNode, root: TreeNode) -> bool:
            if not root:
                return False
            if dfs(head, root):
                return True
            return search(head, root.left) or search(head, root.right)



        return search(head, root)