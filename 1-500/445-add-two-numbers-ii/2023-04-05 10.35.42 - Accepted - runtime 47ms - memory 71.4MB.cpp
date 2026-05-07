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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        string a=listNodeToString(l1),b=listNodeToString(l2);
        return stringToListNode(addStrings(a,b));
    }

    string listNodeToString(ListNode* head) {
        string result = "";
        ListNode* curr = head;

        while (curr != nullptr) {
            // Convert the integer value to string and append to the result
            result += to_string(curr->val);

            // Move to the next node
            curr = curr->next;
        }

        return result;
    }

    string addStrings(string num1, string num2) {
        string result = "";
        int carry = 0;
        int i = num1.length() - 1;
        int j = num2.length() - 1;

        // Loop through the input strings from right to left
        while (i >= 0 || j >= 0 || carry > 0) {
            int digit1 = i >= 0 ? num1[i] - '0' : 0;
            int digit2 = j >= 0 ? num2[j] - '0' : 0;
            int sum = digit1 + digit2 + carry;

            carry = sum / 10;
            sum %= 10;

            // Append the current sum to the result string
            result = to_string(sum) + result;

            i--;
            j--;
        }

        return result;
    }


    ListNode* stringToListNode(const string& s) {
        ListNode* dummy = new ListNode(0); // dummy node to keep track of the head
        ListNode* curr = dummy; // current node to append new nodes

        // Iterate through the string characters
        for (char c : s) {
            int digit = c - '0'; // convert character to integer

            // Create a new node with the digit value
            ListNode* newNode = new ListNode(digit);

            // Append the new node to the current node
            curr->next = newNode;

            // Move to the next node
            curr = curr->next;
        }

        return dummy->next; // return the head of the constructed linked list
    }
};