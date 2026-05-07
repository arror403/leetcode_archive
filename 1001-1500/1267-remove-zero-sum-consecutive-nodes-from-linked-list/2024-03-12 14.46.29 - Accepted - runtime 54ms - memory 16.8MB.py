class Solution:
    ##### power by Claude #####
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        sum_map = {0: dummy}
        curr_sum = 0

        while curr:
            curr_sum += curr.val
            if curr_sum in sum_map:
                node = sum_map[curr_sum].next
                temp_sum = curr_sum
                while node != curr:
                    temp_sum += node.val
                    del sum_map[temp_sum]
                    node = node.next
                sum_map[curr_sum].next = curr.next
            else:
                sum_map[curr_sum] = curr
            curr = curr.next

        return dummy.next


    #     t=self.LinkedToArr(head)

    #     res=[[i,j-1] for i in range(len(t)) for j in range(i+1, len(t)+1) if sum(t[i:j])==0]

    #     r=set()
    #     for x in res: r|=set(range(x[0],x[1]+1))

    #     print(r,res)

    #     print([v for i,v in enumerate(t) if i not in r])

    #     return self.ArrToLinked([v for i,v in enumerate(t) if i not in r])



    # def ArrToLinked(self, l):
    #     if not l: return None
    #     dummy = ListNode(0)
    #     cur = dummy
    #     for n in l:
    #         cur.next = ListNode(n)
    #         cur = cur.next
    #     return dummy.next
        
        
    # def LinkedToArr(self, head):
    #     arr = []
    #     curr = head
    #     while (curr != None): 
    #         arr.append(curr.val)
    #         curr = curr.next
    #     return arr