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
    public int getDecimalValue(ListNode head) {
        List<Integer> res = LinkedToArrayList(head);
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < res.size(); i++) {
            sb.append(res.get(i).toString());
        }
        
        String str = sb.toString();
        int decNum = Integer.parseInt(str, 2);
        
        return decNum;
    }

    public List<Integer> LinkedToArrayList(ListNode head) {
        List<Integer> x = new ArrayList<>();
        
        while (head != null) {
            x.add(head.val);
            head = head.next;
        }
        
        return x;
    }
}