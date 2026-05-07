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
public class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        List<Integer> m = linkedToArrayList(head);
        int temp = m.get(m.size() - k);
        m.set(m.size() - k, m.get(k - 1));
        m.set(k - 1, temp);
        return arrayListToLinked(m);
    }

    private List<Integer> linkedToArrayList(ListNode head) {
        List<Integer> list = new ArrayList<>();
        while (head != null) {
            list.add(head.val);
            head = head.next;
        }
        return list;
    }

    private ListNode arrayListToLinked(List<Integer> list) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int n : list) {
            cur.next = new ListNode(n);
            cur = cur.next;
        }
        return dummy.next;
    }
}