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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        vector<int> x=LinkedToVec(list1),y=LinkedToVec(list2),res;
        
        // for i in range(a): res.append(list1[i])

        for(int i=0;i<a;i++) res.push_back(x[i]);

        // for i in list2: res.append(i)
        for (auto i:y) res.push_back(i);

        // for i in range(b+1,len(list1)): res.append(list1[i])
        for (int i=b+1;i<x.size();i++) res.push_back(x[i]);   
        
        // return self.ArrToLinked(res)
        return  VecToLinked(res);
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