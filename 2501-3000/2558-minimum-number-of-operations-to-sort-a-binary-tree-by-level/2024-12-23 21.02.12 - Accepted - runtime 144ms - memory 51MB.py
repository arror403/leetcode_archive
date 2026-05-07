class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        return sum(self.minSwap(level) for level in self.levelOrder(root))
    

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        queue = deque([root])
        
        while queue:
            level = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(level)
            
        return result
    

    def minSwap(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1: return 0
            
        # Create position map and sorted array in one pass
        position = {v:i for i,v in enumerate(arr)}
        sorted_arr = sorted(arr)
        swaps = 0
        
        # Use visited set to track handled elements
        visited = set()
        
        for i in range(n):
            if i in visited or arr[i] == sorted_arr[i]:
                continue
                
            # Count elements in this cycle
            cycle_size = 0
            j = i
            
            while j not in visited:
                visited.add(j)
                j = position[sorted_arr[j]]
                cycle_size += 1
                
            # Number of swaps needed for this cycle is cycle_size - 1
            swaps += cycle_size - 1
            
        return swaps