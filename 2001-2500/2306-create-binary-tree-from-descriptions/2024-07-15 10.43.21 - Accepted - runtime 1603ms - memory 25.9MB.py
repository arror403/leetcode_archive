# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)

            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

            children.add(child)

        root = None
        for node in nodes:
            if node not in children:
                root = nodes[node]
                break

        return root
        # d=defaultdict(list)
        # for x in descriptions: d[x[0]].append([x[1],x[2]])

        # p=[i[0] for i in descriptions]
        # c=[i[1] for i in descriptions]
        # root=next(x for x in p if x not in c)

        # if d[root][1][1]: d[root][0],d[root][1]=d[root][1],d[root][0]
        # res=Tree()
        # res.add(root)
        # d.pop(root)

        # while d:





        # print(d)
        # return res