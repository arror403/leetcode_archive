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
    int pairSum(ListNode* head) {
        vector<int>m=LinkedToVec(head);
        int res=INT_MIN;
        

        for (int i=0;i<m.size()/2+1;i++){
            if ((m[i]+m[m.size()-i-1])>res)
                res=(m[i]+m[m.size()-i-1]);
        }

                
        return res;
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