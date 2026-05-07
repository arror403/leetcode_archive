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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        int len = inorder.length;
        return buildSubTree(inorder, 0, len - 1, postorder, 0, len - 1);
    }

    private TreeNode buildSubTree(int[] inorder, int inStart, int inEnd, int[] postorder, int postStart, int postEnd) {
        if (inStart > inEnd) {
            return null;
        }
        int rootVal = postorder[postEnd];
        TreeNode root = new TreeNode(rootVal);
        int rootIndex = inStart;
        while (inorder[rootIndex] != rootVal) {
            rootIndex++;
        }
        int leftSize = rootIndex - inStart;
        root.left = buildSubTree(inorder, inStart, rootIndex - 1, postorder, postStart, postStart + leftSize - 1);
        root.right = buildSubTree(inorder, rootIndex + 1, inEnd, postorder, postStart + leftSize, postEnd - 1);
        return root;
    }
}