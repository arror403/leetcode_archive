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
    ListNode* reverseEvenLengthGroups(ListNode* xxx) {
        vector<int> m = LinkedToArr(xxx);
        int x = 0;
        vector<int> res;
        while (true) {
            x++;
            int i = Sum(x-1), j = Sum(x);
            if (j > m.size()) {
                if ((m.size() - i) % 2 == 0) {
                    vector<int> tmp(m.begin() + i, m.end());
                    reverse(tmp.begin(), tmp.end());
                    res.insert(res.end(), tmp.begin(), tmp.end());
                    break;
                } else {
                    res.insert(res.end(), m.begin() + i, m.end());
                    break;
                }
            } else if (x % 2 == 0) {
                vector<int> tmp(m.begin() + i, m.begin() + j);
                reverse(tmp.begin(), tmp.end());
                res.insert(res.end(), tmp.begin(), tmp.end());
            } else {
                res.insert(res.end(), m.begin() + i, m.begin() + j);
            }
        }
        return ArrToLinked(res);
    }
    
    int Sum(int x) {
        return int(x * (x + 1) / 2);
    }
        
    ListNode* ArrToLinked(vector<int> l) {
        ListNode *cur = new ListNode(0);
        ListNode *dummy = cur;
        for (int n : l) {
            cur->next = new ListNode(n);
            cur = cur->next;
        }
        return dummy->next;
    }
        
    vector<int> LinkedToArr(ListNode* head) {
        vector<int> arr;
        ListNode *curr = head;
        while (curr != nullptr) { 
            arr.push_back(curr->val);
            curr = curr->next;
        }
        return arr;
    }
};