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
    public ListNode removeElements(ListNode head, int val) {
        ArrayList<Integer> m = linkedToArrayList(head);
        ArrayList<Integer> res = new ArrayList<>();
        for (Integer i : m) {
            if (i == val) continue;
            else res.add(i);
        }
        return arrayListToLinked(res);
    }

    public ArrayList<Integer> linkedToArrayList(ListNode head) {
        ArrayList<Integer> result = new ArrayList<>();
        ListNode current = head;
        while (current != null) {
            result.add(current.val);
            current = current.next;
        }
        return result;
    }

    public ListNode arrayListToLinked(ArrayList<Integer> arr) {
        if (arr == null || arr.isEmpty()) return null;
        ListNode head = new ListNode(arr.get(0));
        ListNode current = head;
        for (int i = 1; i < arr.size(); i++) {
            current.next = new ListNode(arr.get(i));
            current = current.next;
        }
        return head;
    }
}