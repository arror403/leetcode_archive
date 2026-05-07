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
    public ListNode swapPairs(ListNode head) {
        List<Integer> m = linkedToArrayList(head);
        List<Integer> res = new ArrayList<>();
        for (int i = 1; i < m.size(); i += 2) {
            res.add(m.get(i));
            res.add(m.get(i - 1));
        }
        if (m.size() % 2 == 1)
            res.add(m.get(m.size() - 1));

        return arrayListToLinkedList(res);
    }

    private List<Integer> linkedToArrayList(ListNode head) {
        List<Integer> list = new ArrayList<>();
        while (head != null) {
            list.add(head.val);
            head = head.next;
        }
        return list;
    }

    private ListNode arrayListToLinkedList(List<Integer> list) {
        ListNode cur, dummy;
        cur = dummy = new ListNode(0);
        for (int n : list) {
            cur.next = new ListNode(n);
            cur = cur.next;
        }
        return dummy.next;
    }
}