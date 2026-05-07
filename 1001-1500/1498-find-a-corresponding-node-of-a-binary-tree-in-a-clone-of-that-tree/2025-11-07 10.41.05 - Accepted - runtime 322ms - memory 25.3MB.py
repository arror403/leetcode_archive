# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def inorder(o, c):
            if o:
                inorder(o.left, c.left)
                if o is target:
                    self.res = c
                inorder(o.right, c.right)
                
        inorder(original, cloned)

        return self.res
        
        # p = [["root"]]
        # def levelOrder(root):
        #     q = []
        #     res = []
        #     q.append(root)
        #     curr_level = 0

        #     while q:
        #         tmp = []
        #         res.append([])
        #         for _ in range(len(q)):
        #             # Add front of queue and remove it from queue
        #             node = q.pop(0)
        #             res[curr_level].append(node.val)
        #             # Enqueue left child
        #             if node.left:
        #                 q.append(node.left)
        #                 tmp.append("L")
        #             else: tmp.append("l_end")
        #             # Enqueue right child
        #             if node.right:
        #                 q.append(node.right)
        #                 tmp.append("R")
        #             else: tmp.append("r_end")
                
        #         p.append(tmp)
        #         curr_level += 1

        #     return res

        # # for x in levelOrder(original):


        # print(levelOrder(original))
        # print(p)

        # return TreeNode()