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
    public ListNode deleteMiddle(ListNode head) {
        List<Integer> arr = linkedToArr(head);
        arr.remove(arr.size() / 2);
        return arrToLinked(arr);
    }
    
    private List<Integer> linkedToArr(ListNode head) {
        List<Integer> arr = new ArrayList<>();
        while (head != null) {
            arr.add(head.val);
            head = head.next;
        }
        return arr;
    }
    
    private ListNode arrToLinked(List<Integer> arr) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int n : arr) {
            cur.next = new ListNode(n);
            cur = cur.next;
        }
        return dummy.next;
    }
}