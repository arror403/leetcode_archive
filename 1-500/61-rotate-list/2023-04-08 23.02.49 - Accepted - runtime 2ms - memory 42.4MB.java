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
    public ListNode rotateRight(ListNode head, int k) {
        ArrayList<Integer> res = linkedToArrayList(head);
        if (res.size() == 0) return null;
        k = k % res.size();
        Collections.rotate(res, k);
        return arrayListToLinked(res);
    }

    private ArrayList<Integer> linkedToArrayList(ListNode head) {
        ArrayList<Integer> arr = new ArrayList<>();
        ListNode curr = head;
        while (curr != null) {
            arr.add(curr.val);
            curr = curr.next;
        }
        return arr;
    }

    private ListNode arrayListToLinked(ArrayList<Integer> arr) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        for (int num : arr) {
            curr.next = new ListNode(num);
            curr = curr.next;
        }
        return dummy.next;
    }
}