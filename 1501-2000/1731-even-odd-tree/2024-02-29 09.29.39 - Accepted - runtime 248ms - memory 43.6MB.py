# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        t=self.group_by_level(root)

        even_indices = t[::2]
        odd_indices = t[1::2]

        # print(t,even_indices,odd_indices)

        if not all(j%2==1 for i in even_indices for j in i): return False
        if not all(j%2==0 for i in odd_indices for j in i): return False
        
        for v in even_indices:
            if len(v)!=len(set(v)) or v!=sorted(v):
                return False

        for v in odd_indices:
            if len(v)!=len(set(v)) or v!=sorted(v, reverse=True):
                return False


        return True



    def group_by_level(self, root):
        if not root: return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        return result