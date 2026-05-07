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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return buildTreeHelper(preorder, inorder, 0, inorder.size() - 1);
    }


    TreeNode* buildTreeHelper(vector<int>& preorder, vector<int>& inorder, int inStart, int inEnd) {
        if (inStart > inEnd) return nullptr;

        int rootVal = preorder[0];
        preorder.erase(preorder.begin());
        int ind;
        for (int i = inStart; i <= inEnd; i++) {
            if (inorder[i] == rootVal) {
                ind = i;
                break;
            }
        }

        TreeNode* root = new TreeNode(rootVal);
        root->left = buildTreeHelper(preorder, inorder, inStart, ind - 1);
        root->right = buildTreeHelper(preorder, inorder, ind + 1, inEnd);
        return root;
    }
};