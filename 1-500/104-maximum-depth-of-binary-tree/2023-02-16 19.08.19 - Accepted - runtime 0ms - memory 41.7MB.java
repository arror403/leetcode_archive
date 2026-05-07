/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        return height(root);
    }
    int height(TreeNode root){
        int leftAns,rightAns;
        if (root==null) return 0;
        leftAns = height(root.left);
        rightAns = height(root.right);
        return Math.max(leftAns, rightAns) + 1;
    }
}