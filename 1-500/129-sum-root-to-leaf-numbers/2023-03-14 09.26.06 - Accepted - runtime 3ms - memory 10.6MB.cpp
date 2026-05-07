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
    int sumNumbers(TreeNode* root) {
        vector<vector<int>> paths;
        vector<int> path;
        string s;
        int res=0;
        getPaths(root, paths, path);
        for (auto i:paths){
            s="";
            for (int j:i) {
                s += to_string(j);
            }
            res += stoi(s);
        }
        return res;
        
    }
    void getPaths(TreeNode* node, vector<vector<int>>& paths, vector<int>& path) {
        if (!node) {
            return;
        }
        path.push_back(node->val);
        if (!node->left && !node->right) {
            paths.push_back(path);
        } else {
            getPaths(node->left, paths, path);
            getPaths(node->right, paths, path);
        }
        path.pop_back();
    }

};