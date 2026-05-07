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
    int getDecimalValue(ListNode* head) {
        vector<int> res=LinkedToVec(head);
        // concatenate the vector elements into a string
        string str;
        for (int i = 0; i < res.size(); i++) {
            str += to_string(res[i]);
        }
        // for(auto i:str) cout << i;
        
        bitset<32> bits(str); // create a bitset with the binary string
        int decNum = bits.to_ulong(); // convert the bitset to an unsigned long integer

        return decNum;
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