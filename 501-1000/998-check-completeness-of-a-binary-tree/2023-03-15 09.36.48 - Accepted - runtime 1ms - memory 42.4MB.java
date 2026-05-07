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
    public boolean isCompleteTree(TreeNode root) {
        return isCompleteBinaryTree(root);
    }
    // Check if the binary tree is complete
    boolean isCompleteBinaryTree(TreeNode root) {
        if (root == null) return true;

        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);

        boolean flag = false;

        while (!q.isEmpty()) {
            TreeNode temp = q.poll();

            if (temp.left != null) {
                if (flag) return false;
                q.offer(temp.left);
            }
            else flag = true;

            if (temp.right != null) {
                if (flag) return false;
                q.offer(temp.right);
            }
            else flag = true;
        }
        return true;
    }
}