class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        return sum(self.minSwap(r) for r in self.LevelOrder(root))
        

    def LevelOrder(self, root):
        if root is None: return
        res=[]
        q=[]
        q.append(root)
        while len(q)>0:
            level=[]
            for _ in range(len(q)):
                node=q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res


    def minSwap(self, arr):
        ans=0
        n=len(arr)
        temp=arr[:]
        h={}
        temp.sort()

        for i in range(n): h[arr[i]] = i

        init=0

        for i in range(n):
            if (arr[i] != temp[i]):
                ans += 1
                init = arr[i]

                arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i]

                h[init] = h[temp[i]]
                h[temp[i]] = i

        return ans