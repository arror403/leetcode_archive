# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:


        def postorder(root):

            if root.left is None and root.right is None:
                return str(root.val)

            result = ""
            if root.left is not None:
                result += postorder(root.left)

            if root.right is not None:
                result += postorder(root.right)

            result += str(root.val) # + " "

            return result
        


        def evaluate_postfix(expression):
            stack = []
            operators = set(['&','|'])

            for token in expression:
                if token not in operators:
                    stack.append(int(token))
                else:
                    if token == '&':
                        operand2 = stack.pop()
                        operand1 = stack.pop()
                        stack.append(operand1 and operand2)
                    elif token == '|':
                        operand2 = stack.pop()
                        operand1 = stack.pop()
                        stack.append(operand1 or operand2)

            return stack[0]



        t=postorder(root)
        res=''
        m="01|&"

        for i in t: res+=m[int(i)]

        # print(res)

        return evaluate_postfix(res)



