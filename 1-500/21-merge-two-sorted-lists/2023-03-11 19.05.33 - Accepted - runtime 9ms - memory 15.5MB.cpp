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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        vector<int> a,b;
        a=LinkedToVec(list1);
        b=LinkedToVec(list2);
        for (auto i:b){
            a.push_back(i);
        }
        sort(a.begin(),a.end());
        return VecToLinked(a);
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