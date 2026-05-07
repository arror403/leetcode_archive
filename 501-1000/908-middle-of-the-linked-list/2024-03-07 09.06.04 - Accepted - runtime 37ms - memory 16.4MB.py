class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def LinkedToArr(head):
            arr = []
            curr = head
            while (curr != None): 
                arr.append(curr.val)
                curr = curr.next
            return arr

        def ArrToLinked(l):
            cur = dummy = ListNode(0)
            for n in l:
                cur.next = ListNode(n)
                cur = cur.next
            return dummy.next

        t=LinkedToArr(head)
        return ArrToLinked(t[len(t)//2:])