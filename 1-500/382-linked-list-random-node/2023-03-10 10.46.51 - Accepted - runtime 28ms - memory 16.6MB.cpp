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
    int l;
    int *h;
    Solution(ListNode* head) {
        l=findlength(head);
        h=converttoarray(head);
    }
    
    int getRandom() {
        int randomNumber = rand()%l;
        return h[randomNumber];
    }

    //Function to find the length of the linked list
    int findlength(ListNode *head){
        ListNode* temp=head;
        int totallength=0;
        while(temp!=NULL){
        totallength++;
        temp=temp->next;
        }
        return totallength;
    }

    //Function to convert the linked list to array and later print it
    int* converttoarray(ListNode *head){
        int len=findlength(head);
        int i=0;
        ListNode *temp=head;
        int *A=new int[len];
        while(temp!=NULL){
            A[i++]=temp->val;
            temp=temp->next;
        }
        return A;
    }

};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */