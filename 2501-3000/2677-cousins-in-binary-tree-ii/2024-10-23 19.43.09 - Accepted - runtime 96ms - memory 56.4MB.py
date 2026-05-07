# 1. Run BFS 
# 2. While traversing take the sum of the child nodes & also keep storing the node in a buffer
# 3. After each stage of the BFS, traverse the buf & update the node with value sum - (child's sum)
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val=0
        q=deque([root])

        while q:
            n=len(q)
            S=0
            buf=[]
            while n:
                node=q.popleft()
                buf.append(node)
                if node.left:
                    q.append(node.left)
                    S+=node.left.val
                if node.right:
                    q.append(node.right)
                    S+=node.right.val
                n-=1
            
            for node in buf:
                t=S
                if node.left:  t-=node.left.val
                if node.right: t-=node.right.val
                if node.left:  node.left.val=t
                if node.right: node.right.val=t


        return root