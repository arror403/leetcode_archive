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
    vector<int> inorderTraversal(TreeNode* root) {
        return inorder(root);
    }
    void traversal(TreeNode *node, vector<int> &res) {
        if (node) {
        traversal(node->left, res);
        res.push_back(node->val);
        traversal(node->right, res);
        }
    }
    vector<int> inorder(TreeNode* root) {
        vector<int> res;
        traversal(root, res);
        return res;
    }


};