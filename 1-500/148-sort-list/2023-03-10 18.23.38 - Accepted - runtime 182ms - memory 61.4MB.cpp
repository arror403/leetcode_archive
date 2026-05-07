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
    ListNode* sortList(ListNode* head) {
        vector<int> res=LinkedToVec(head);
        sort(res.begin(),res.end());
        return VecToLinked(res);
    }


    ListNode* VecToLinked(vector<int> arr){
        int n=arr.size();
        ListNode* head = NULL;
        ListNode* tail = NULL;
        for(int i=0;i<n;i++){
            ListNode* newNode = new ListNode;
            newNode->val = arr[i];
            newNode->next = NULL;
            if(head == NULL){
                head = newNode;
                tail = newNode;
            }
            else{
                tail->next = newNode;
                tail = newNode;
            }
        }
        return head;
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