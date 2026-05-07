/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
        const result = [];
        this.traversal(root, result);
        return result;    
};

traversal = function(node, result) {
    if (node) {
        this.traversal(node.left, result);
        result.push(node.val);
        this.traversal(node.right, result);
    }
}