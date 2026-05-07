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
    public int pairSum(ListNode head) {
        List<Integer> m = linkedToArrayList(head);
        int res = Integer.MIN_VALUE;

        for (int i = 0; i < m.size() / 2 + 1; i++) {
            if ((m.get(i) + m.get(m.size() - i - 1)) > res)
                res = (m.get(i) + m.get(m.size() - i - 1));
        }

        return res;
    }

    public List<Integer> linkedToArrayList(ListNode head) {
        List<Integer> x = new ArrayList<>();
        while (head != null) {
            x.add(head.val);
            head = head.next;
        }
        return x;
    }
}