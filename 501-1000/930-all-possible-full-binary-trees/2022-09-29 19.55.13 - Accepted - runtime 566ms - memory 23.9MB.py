# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        hm = {}
        # Check whether tree exists for given n value or not.
        if n not in hm:

            # Create a list containing nodes
            List = []

            # If N=1, Only one tree can exist
            # i.e. tree with root.
            if (n == 1):
                List.append(TreeNode(0, None, None))

            # Check if N is odd because binary full
            # tree has N nodes
            elif (n % 2 == 1):

                # Iterate through all the nodes that
                # can be in the left subtree
                for x in range(n):

                    # Remaining Nodes belongs to the
                    # right subtree of the node
                    y = n - 1 - x

                    # Iterate through all left Full Binary Tree
                    #  by recursively calling the function
                    xallPossibleFBT = self.allPossibleFBT(x)
                    yallPossibleFBT = self.allPossibleFBT(y)
                    for Left in range(len(xallPossibleFBT)):

                        # Iterate through all the right Full
                        # Binary tree by recursively calling
                        # the function
                        for Right in range(len(yallPossibleFBT)):

                            # Create a new node
                            node = TreeNode(0, None, None)

                            # Modify the left node
                            node.left = xallPossibleFBT[Left]

                            # Modify the right node
                            node.right = yallPossibleFBT[Right]

                            # Add the node in the list
                            List.append(node)

            #Insert tree in Dictionary.
            hm[n] = List
        return hm[n]
