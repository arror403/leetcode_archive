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
    public ListNode reverseList(ListNode head) {
        int res[];
        res=LinkedToArr(head);
        res=reverseArray(res);
        return ArrToLinked(res);
    }


    public static int[] reverseArray(int[] arr) {
        int[] reversedArr = new int[arr.length];
        int j = arr.length - 1;
        for (int i = 0; i < arr.length; i++) {
            reversedArr[j] = arr[i];
            j--;
        }
        return reversedArr;
    }


    public int[] LinkedToArr(ListNode head) {
        List<Integer> list = new ArrayList<>();
        ListNode curr = head;
        while (curr != null) { 
            list.add(curr.val);
            curr = curr.next;
        }
        int[] arr = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            arr[i] = list.get(i);
        }
        return arr;
    }


    public ListNode ArrToLinked(int[] l) {
        ListNode cur = new ListNode(0);
        ListNode dummy = cur;
        for (int n : l) {
            cur.next = new ListNode(n);
            cur = cur.next;
        }
        return dummy.next;
    }
}