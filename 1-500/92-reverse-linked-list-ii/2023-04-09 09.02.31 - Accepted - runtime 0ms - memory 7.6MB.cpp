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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        vector<int> res=LinkedToVec(head);
        reverse(res.begin()+left-1,res.begin()+right);
        return VecToLinked(res);
    }

    vector<int> LinkedToVec(ListNode* head) {
        vector<int> x;
        while(head!=NULL){
            x.push_back(head->val);
            head=head->next;
        }
        return x;
    }


    ListNode* VecToLinked(vector<int> l) {
        ListNode *cur, *dummy;
        cur = dummy = new ListNode(0);
        for (auto n : l) {
            cur->next = new ListNode(n);
            cur = cur->next;
        }
        return dummy->next;
    }
};