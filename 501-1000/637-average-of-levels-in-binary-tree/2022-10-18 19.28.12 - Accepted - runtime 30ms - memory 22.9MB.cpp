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
    map<int, pair<double, double> > mp;
    vector<double> averageOfLevels(TreeNode* root){
        vector<double> x;
        avg(root, 0);
    
        // Travaersing for levels in map
        for (auto i : mp) {
            // Printing average of all levels
            // cout << (i.second.first / i.second.second) << ' ';
            x.push_back(i.second.first / i.second.second);
        }
        return x;
    }

    // Initialising a map with key as levels of the tree
    // map<int, pair<double, double> > mp;
    
    void avg(TreeNode* r, int l){
        // If the node is NULL
        if (r == NULL)
            return;
    
        // Add the current value to the sum of this level
        mp[l].first += r->val;
    
        // Increase the number of elements in the current level
        mp[l].second++;
    
        // Traverse left
        avg(r->left, l + 1);
    
        // Traverse right
        avg(r->right, l + 1);
    }

    
    // Function to create a new node
    TreeNode* newNode(int data){
        TreeNode* temp = new TreeNode;
        temp->val = data;
        temp->left = temp->right = NULL;
        return temp;
    }


};