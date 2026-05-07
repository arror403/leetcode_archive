"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        
        stack=[]
        res=[]
        stack.append(root)
        
        while stack:
            root=stack.pop()
            res.append(root.val)

            for node in root.children:
                stack.append(node)


        return reversed(res)