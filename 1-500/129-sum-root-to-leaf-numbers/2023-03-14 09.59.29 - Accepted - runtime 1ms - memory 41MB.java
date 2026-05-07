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
    public int sumNumbers(TreeNode root) {
        int res=0,tmp;
        List<List<Integer>> paths = new ArrayList<>();
        if (root != null) {
            List<Integer> path = new ArrayList<>();
            traverse(root, path, paths);
        }
        for (int i = 0; i < paths.size(); i++) {
            tmp=0;
            for (int j = 0; j < paths.get(i).size(); j++) {
                tmp = tmp*10 + paths.get(i).get(j);
            }
            res+=tmp;
        }
        return res;
    
    }
    private void traverse(TreeNode node, List<Integer> path, List<List<Integer>> paths) {
        path.add(node.val);
        if (node.left == null && node.right == null) {
            paths.add(new ArrayList<>(path));
        } else {
            if (node.left != null) {
                traverse(node.left, path, paths);
            }
            if (node.right != null) {
                traverse(node.right, path, paths);
            }
        }
        path.remove(path.size() - 1);
    }
}