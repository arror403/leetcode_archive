/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) []int {
    var result []int
	traversal(root, &result)
	return result
}


func traversal(node *TreeNode, result *[]int) {
	if node != nil {
		traversal(node.Left, result)
		*result = append(*result, node.Val)
		traversal(node.Right, result)
	}
}