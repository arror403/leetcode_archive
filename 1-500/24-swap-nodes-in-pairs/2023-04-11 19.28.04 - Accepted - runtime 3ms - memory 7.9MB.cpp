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
    ListNode* swapPairs(ListNode* head) {
        vector<int> m=LinkedToVec(head),res;
        for (int i=1;i<m.size();i+=2){
            res.push_back(m[i]);
            res.push_back(m[i-1]);
        }
        if (m.size()%2==1) res.push_back(m[m.size()-1]);
            
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