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
    int minDiffInBST(TreeNode* root) {
        int r=INT_MAX,tmp;
        vector<int> res;
        inOrder(root,res);
        for (int i=0;i<res.size()-1;i++){
            tmp=abs(res[i]-res[i+1]);
            if (tmp<r) r=tmp;
        }
        return r;
    }
    void inOrder(TreeNode* root, vector<int>& res){
        if(root==NULL) return;
        inOrder(root->left, res);
        res.push_back(root->val);
        inOrder(root->right, res);
    }
};