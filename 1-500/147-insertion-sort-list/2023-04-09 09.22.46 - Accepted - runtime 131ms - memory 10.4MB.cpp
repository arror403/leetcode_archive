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
    ListNode* insertionSortList(ListNode* head) {
        vector<int> res=LinkedToVec(head);
        insertionSort(res);
        return VecToLinked(res);
    }


    void insertionSort(vector<int>& arr) {
        int n = arr.size();
        int i, key, j;
        for (i = 1; i < n; i++) {
            key = arr[i];
            j = i - 1;
            // Move elements of arr[0..i-1] that are greater than key
            // to one position ahead of their current position
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
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