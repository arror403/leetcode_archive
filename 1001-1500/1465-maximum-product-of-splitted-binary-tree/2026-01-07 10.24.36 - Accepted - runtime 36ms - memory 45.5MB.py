def get_subtree_sum(node: TreeNode, subtree_sums: list):
    if node is None: return 0

    total_sum = node.val
    total_sum += get_subtree_sum(node.left, subtree_sums)
    total_sum += get_subtree_sum(node.right, subtree_sums)
    subtree_sums.append(total_sum)

    return total_sum


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sums = []
        total_sum = get_subtree_sum(root, subtree_sums)

        return max([s * (total_sum - s) for s in subtree_sums]) % (10**9 + 7)