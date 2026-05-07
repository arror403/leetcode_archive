/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        invert_tree(root);
        return root;

    }
    void invert_tree(TreeNode* node) {
        // Check whether the node "exists"
        if (node == NULL) {
            return;
        }

        // Swap left and right children
        TreeNode* temp = node->left;
        node->left = node->right;
        node->right = temp;

        // Recursively call the function on both children
        invert_tree(node->left);
        invert_tree(node->right);
    }
};

