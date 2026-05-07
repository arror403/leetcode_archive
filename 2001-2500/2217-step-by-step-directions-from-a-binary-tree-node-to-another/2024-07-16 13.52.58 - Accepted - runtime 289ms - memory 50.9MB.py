class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        p1,p2=[],[]
        self.findPath(root, p1, startValue)
        self.findPath(root, p2, destValue)
        l1,l2=len(p1),len(p2)

        i=0
        while i<l1 and i<l2 and p1[i]==p2[i]: i+=1
        
        steps_up='U'*(l1-i)
        steps_down=""

        for j in range(i, l2):
            parent=p2[j-1]
            if p2[j]==parent.left:
                steps_down+='L'
            else:
                steps_down+='R'

        return steps_up+steps_down


    def findPath(self, root, path, k):
        if root is None: return False

        path.append(root)
        
        if root.val==k: return True
        
        if (root.left and self.findPath(root.left, path, k) or 
            root.right and self.findPath(root.right, path, k)):
            return True    
    
        path.pop()

        return False