class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        q=[root]
        res=[]

        while q:
            row=[]
            for i in range(len(q)):
                curr=q.pop(0)
                row.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    
            res.append(max(row))
            

        return res