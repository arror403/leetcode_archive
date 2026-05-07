class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        def dfs(node, distance):
            if node is None: return [0]*(distance+1)

            if node.left is None and node.right is None:
                res=[0]*(distance+1)
                res[1]+=1
                return res

            left = dfs(node.left, distance)
            right = dfs(node.right, distance)

            nonlocal result

            for l in range(1,len(left)):
                for r in range(1, len(right)):
                    if(l+r)<=distance:
                        result+=left[l]*right[r]
                    
            res=[0]*(distance+1)
            for i in range(1, distance):
                res[i+1]=left[i]+right[i]

            return res

        result=0
        dfs(root,distance)

        return result