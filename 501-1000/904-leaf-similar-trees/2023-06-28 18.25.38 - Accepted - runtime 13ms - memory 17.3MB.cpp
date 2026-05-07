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
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        return getLeafNodes(root1) == getLeafNodes(root2);
    }

    vector<int> getLeafNodes(TreeNode* root) {
        vector<int> leaves;
        
        if (!root->left && !root->right) {
            return { root->val };
        }
        
        if (!root->left) {
            leaves = getLeafNodes(root->right);
        }
        
        if (!root->right) {
            leaves = getLeafNodes(root->left);
        }
        
        if (root->left && root->right) {
            auto leftLeaves = getLeafNodes(root->left);
            auto rightLeaves = getLeafNodes(root->right);
            leaves.insert(leaves.end(), leftLeaves.begin(), leftLeaves.end());
            leaves.insert(leaves.end(), rightLeaves.begin(), rightLeaves.end());
        }
        
        return leaves;
    }
};