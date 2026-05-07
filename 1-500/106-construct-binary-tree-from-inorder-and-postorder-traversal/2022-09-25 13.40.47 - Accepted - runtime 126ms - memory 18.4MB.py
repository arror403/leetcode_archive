# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def buildTreeFromInorderAndPostorder(inorder, post, n):
            # Create Stack of type Node
            st = []
            # Create Set of type Node
            set = []
            # Initialise postIndex with n - 1
            postIndex = n - 1
            # Initialise root with NULL
            root = None
            p = n-1
            i = n-1
            while p >= 0:
                # Initialise node with NULL
                node = None
                #  Run loop
                while True:
                    # initialize new node
                    node = TreeNode(post[p])
                    # check if root is equal to null
                    if root == None:
                        root = node
                    # If size of set is greater than 0
                    if len(st) > 0:
                        # If st top is present in the set s
                        if st[-1] in set:
                            set.remove(st[-1])
                            st[-1].left = node
                            st.pop()
                        else:
                            st[-1].right = node
                    st.append(node)
                    p -= 1
                    if post[p+1] == inorder[i] or p < 0:
                        break
                node = None
                # If the stack is not empty and st top data is equal to in[i]
                while len(st) > 0 and i >= 0 and st[-1].val == inorder[i]:
                    node = st[-1]
                    # Pop elements from stack
                    st.pop()
                    i -= 1
                # if node not equal to None
                if node != None:
                    set.append(node)
                    st.append(node)
            # Return root
            return root
        return buildTreeFromInorderAndPostorder(inorder,postorder,len(inorder))