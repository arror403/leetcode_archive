class Solution(object):
    def pathSum(self, root, target):
        self.res=0
        cache={0:1}
        self.dfs(root, target, 0, cache)
        
        return self.res
    
    
    def dfs(self, root, target, currPathSum, cache):
        if root==None: return

        currPathSum += root.val
        oldPathSum = currPathSum - target

        self.res += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)

        cache[currPathSum] -= 1