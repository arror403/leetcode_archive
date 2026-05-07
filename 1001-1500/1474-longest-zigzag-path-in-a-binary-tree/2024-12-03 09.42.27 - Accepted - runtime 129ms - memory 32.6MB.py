class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(node, is_left, length):
            if not node:
                return length - 1
            
            nonlocal max_len
            max_len = max(max_len, length)
            
            if is_left:
                # If we came from a left child, go right
                right_length = dfs(node.right, False, length + 1)
                # Or start a new path from this node going left
                left_length = dfs(node.left, True, 1)
            else:
                # If we came from a right child, go left
                left_length = dfs(node.left, True, length + 1)
                # Or start a new path from this node going right
                right_length = dfs(node.right, False, 1)
            
            return length

        max_len = 0
        dfs(root, True, 0)  # Start assuming we came from a left child
        dfs(root, False, 0)  # Also start assuming we came from a right child


        return max_len



        # def helper(node, is_left):
            
        #     nonlocal max_len
        #     max_len = max(max_len, len(path))

        #     if is_left:
        #         if node.right:
        #             path.append(node.val)
        #             helper(node.right, True)
        #     else:
        #         if node.left:
        #             path.append(node.val)
        #             helper(node.left, False)

        # max_len = 0
        # path = []
        # helper(root, False) # travel right 
        # # path.clear()
        # helper(root, True) # travel left

        # return max_len