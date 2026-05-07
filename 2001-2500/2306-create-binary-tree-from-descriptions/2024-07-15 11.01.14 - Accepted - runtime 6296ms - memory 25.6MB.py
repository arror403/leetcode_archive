class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d=defaultdict(list)
        for x in descriptions: d[x[0]].append([x[1],x[2]])

        p=[i[0] for i in descriptions]
        c=[i[1] for i in descriptions]
        root_val=next(x for x in p if x not in c)

        # Create a dictionary to store TreeNode references by their values
        nodes={root_val:TreeNode(root_val)}

        # Create all nodes and set children relationships
        for p,c in d.items():
            if p not in nodes: nodes[p]=TreeNode(p)

            parent_node=nodes[p]

            for child,is_left in c:
                if child not in nodes: nodes[child]=TreeNode(child)

                child_node=nodes[child]

                if is_left:
                    parent_node.left = child_node
                else:
                    parent_node.right = child_node


        return nodes[root_val]