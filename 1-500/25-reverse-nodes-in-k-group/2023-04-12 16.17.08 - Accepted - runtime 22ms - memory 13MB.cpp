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
    ListNode* reverseKGroup(ListNode* head, int k) {
        vector<int> m = LinkedToArr(head);
        vector<int> res;
        int l = 0;
        int r, s;
        r = m.size() / k;
        s = m.size() % k;
        while (r > 0) {
            vector<int> tmp(m.begin() + l, m.begin() + l + k);
            reverse(tmp.begin(), tmp.end());
            res.insert(res.end(), tmp.begin(), tmp.end());
            l += k;
            r--;
        }
        res.insert(res.end(), m.begin() + m.size() - s, m.end());
        return ArrToLinked(res);
    }


    ListNode* ArrToLinked(const vector<int>& l) {
        ListNode* cur = new ListNode(0);
        ListNode* dummy = cur;
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