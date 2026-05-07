/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return stringToListNode(addStrings(listNodeToString(l1),listNodeToString(l2)));
    }

    public String listNodeToString(ListNode head) {
        StringBuilder result = new StringBuilder();
        ListNode curr = head;

        while (curr != null) {
            // Convert the integer value to string and append to the result
            result.append(curr.val);

            // Move to the next node
            curr = curr.next;
        }

        return result.toString();
    }

    public String addStrings(String num1, String num2) {
        StringBuilder result = new StringBuilder();
        int carry = 0;
        int i = num1.length() - 1;
        int j = num2.length() - 1;

        // Loop through the input strings from right to left
        while (i >= 0 || j >= 0 || carry > 0) {
            int digit1 = i >= 0 ? num1.charAt(i) - '0' : 0;
            int digit2 = j >= 0 ? num2.charAt(j) - '0' : 0;
            int sum = digit1 + digit2 + carry;

            carry = sum / 10;
            sum %= 10;

            // Append the current sum to the result string
            result.insert(0, sum);

            i--;
            j--;
        }

        return result.toString();
    }

    public ListNode stringToListNode(String s) {
        ListNode dummy = new ListNode(0); // dummy node to keep track of the head
        ListNode curr = dummy; // current node to append new nodes

        // Iterate through the string characters
        for (char c : s.toCharArray()) {
            int digit = c - '0'; // convert character to integer

            // Create a new node with the digit value
            ListNode newNode = new ListNode(digit);

            // Append the new node to the current node
            curr.next = newNode;

            // Move to the next node
            curr = curr.next;
        }

        return dummy.next; // return the head of the constructed linked list
    }
}