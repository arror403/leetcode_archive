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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        vector<int> m = LinkedToArr(head);
        vector<vector<int>> res = split(m, k);
        vector<ListNode*> result;
        for (const auto& v : res) {
            result.push_back(ArrToLinked(v));
        }
        return result;
    }

private:
    vector<vector<int>> split(vector<int>& a, int n) {
        int k = a.size() / n;
        int m = a.size() % n;
        vector<vector<int>> result(n);
        int start = 0;
        for (int i = 0; i < n; ++i) {
            int end = start + k + (i < m ? 1 : 0);
            result[i] = vector<int>(a.begin() + start, a.begin() + end);
            start = end;
        }
        return result;
    }

    ListNode* ArrToLinked(const vector<int>& l) {
        ListNode* dummy = new ListNode(0);
        ListNode* cur = dummy;
        for (int n : l) {
            cur->next = new ListNode(n);
            cur = cur->next;
        }
        return dummy->next;
    }

    vector<int> LinkedToArr(ListNode* head) {
        vector<int> arr;
        ListNode* curr = head;
        while (curr != nullptr) {
            arr.push_back(curr->val);
            curr = curr->next;
        }
        return arr;
    }
};