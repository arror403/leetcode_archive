# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return -1
            
        # Use deque for level-order traversal
        q = deque([root])
        # Use list for storing level sums
        level_sums = []
        
        # Level-order traversal
        while q:
            level_sum = 0
            level_size = len(q)
            
            # Process current level
            for _ in range(level_size):
                node = q.popleft()
                level_sum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level_sums.append(level_sum)
        
        # If we don't have enough levels
        if len(level_sums) < k: return -1
            
        # Sort in descending order and return kth largest
        level_sums.sort(reverse=True)


        return level_sums[k-1]