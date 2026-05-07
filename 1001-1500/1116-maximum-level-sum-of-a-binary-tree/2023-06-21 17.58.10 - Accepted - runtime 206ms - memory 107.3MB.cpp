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
    int maxLevelSum(TreeNode* root) {
        if (!root) {
            return 0;
        }

        std::queue<TreeNode*> queue;
        queue.push(root);
        int max_sum = std::numeric_limits<int>::min();
        int max_level = 0;
        int level = 1;

        while (!queue.empty()) {
            int size = queue.size();
            int level_sum = 0;

            for (int i = 0; i < size; i++) {
                TreeNode* node = queue.front();
                queue.pop();
                level_sum += node->val;

                if (node->left) {
                    queue.push(node->left);
                }
                if (node->right) {
                    queue.push(node->right);
                }
            }

            if (level_sum > max_sum) {
                max_sum = level_sum;
                max_level = level;
            }

            level++;
        }

        return max_level;
    }
};