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
    ListNode* deleteMiddle(ListNode* head) {
        vector<int> arr = linkedToArr(head);
        arr.erase(arr.begin() + arr.size() / 2);
        return arrToLinked(arr);
    }
    

    vector<int> linkedToArr(ListNode* head) {
        vector<int> arr;
        while (head != nullptr) {
            arr.push_back(head->val);
            head = head->next;
        }
        return arr;
    }
    
    
    ListNode* arrToLinked(const vector<int>& arr) {
        ListNode* dummy = new ListNode(0);
        ListNode* cur = dummy;
        for (int n : arr) {
            cur->next = new ListNode(n);
            cur = cur->next;
        }
        return dummy->next;
    }
};