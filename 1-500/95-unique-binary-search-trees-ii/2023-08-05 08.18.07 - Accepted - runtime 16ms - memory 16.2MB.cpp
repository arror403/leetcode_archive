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
    vector<TreeNode*> generateTrees(int n) {
        return constructTrees(1, n);
    }

private:
    vector<TreeNode*> constructTrees(int start, int end) {
        vector<TreeNode*> trees;

        // If start > end, return an empty subtree (NULL)
        if (start > end) {
            trees.push_back(NULL);
            return trees;
        }

        // Iterate through all values from start to end
        for (int i = start; i <= end; ++i) {
            // Construct left subtree recursively
            vector<TreeNode*> leftSubtree = constructTrees(start, i - 1);
            
            // Construct right subtree recursively
            vector<TreeNode*> rightSubtree = constructTrees(i + 1, end);

            // Connect left and right subtrees to the current root (ith node)
            for (TreeNode* left : leftSubtree) {
                for (TreeNode* right : rightSubtree) {
                    TreeNode* node = new TreeNode(i); // Making value i as root
                    node->left = left; // Connect left subtree
                    node->right = right; // Connect right subtree
                    trees.push_back(node); // Add this tree to the list
                }
            }
        }
        return trees;
    }
};

// Function to delete the tree and release memory
void deleteTree(TreeNode* root) {
    if (root) {
        deleteTree(root->left);
        deleteTree(root->right);
        delete root;
    }
}

// Function to print the tree in preorder
void printPreorder(TreeNode* root) {
    if (root) {
        cout << root->val << " ";
        printPreorder(root->left);
        printPreorder(root->right);
    }
}