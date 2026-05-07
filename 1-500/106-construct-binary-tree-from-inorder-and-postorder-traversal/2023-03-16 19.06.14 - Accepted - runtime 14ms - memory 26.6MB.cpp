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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        unordered_map<int, int> in_map;
        for (int i = 0; i < inorder.size(); i++) {
            in_map[inorder[i]] = i;
        }
        return build(inorder, postorder, 0, inorder.size() - 1, 0, postorder.size() - 1, in_map);
    }

    TreeNode* build(vector<int>& inorder, vector<int>& postorder, int in_start, int in_end, int post_start, int post_end, unordered_map<int, int>& in_map) {
        if (in_start > in_end || post_start > post_end) {
            return NULL;
        }
        TreeNode* root = new TreeNode(postorder[post_end]);
        int in_root = in_map[root->val];
        int nums_left = in_root - in_start;
        root->left = build(inorder, postorder, in_start, in_root - 1, post_start, post_start + nums_left - 1, in_map);
        root->right = build(inorder, postorder, in_root + 1, in_end, post_start + nums_left, post_end - 1, in_map);
        return root;
    }

};