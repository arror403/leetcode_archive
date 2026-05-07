/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> m=LinkedToVec(head);
        return nextLargerElement(m);
    }

    vector<int> nextLargerElement(vector<int>& arr) {
        vector<int> result(arr.size(), 0);
        stack<pair<int, int>> s;
        for (int i = 0; i < arr.size(); i++) {
            while (!s.empty() && s.top().first < arr[i]) {
                pair<int, int> d = s.top();
                s.pop();
                result[d.second] = arr[i];
            }
            s.push(make_pair(arr[i], i));
        }
        return result;
    }


    vector<int> LinkedToVec(ListNode* head) {
        vector<int> x;
        while(head!=NULL){
            x.push_back(head->val);
            head=head->next;
        }
        return x;
    }
};