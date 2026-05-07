# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def removeZeroSum(head, K):
            # Root node initialise to 0
            root = ListNode(0)
            # Append at the front of the given
            # Linked List
            root.next = head
            # Map to store the sum and reference
            # of the Node
            umap = dict()
            umap[0] = root
            # To store the sum while traversing
            sum = 0
            # Traversing the Linked List
            while (head != None):
                # Find sum
                sum += head.val
                # If found value with (sum - K)
                if ((sum - K) in umap):
                    prev = umap[sum - K]
                    start = prev
                    # Delete all the node
                    # traverse till current node
                    aux = sum
                    # Update sum
                    sum = sum - K
                    # Traverse till current head
                    while (prev != head):
                        prev = prev.next
                        aux += prev.val
                        if (prev != head):
                            # umap.remove(aux)
                            del umap[aux]
                    # Update the start value to
                    # the next value of current head
                    start.next = head.next
                # If (sum - K) value not found
                else:
                    umap[sum] = head
                head = head.next
            # Return the value of updated
            # head node
            return root.next
        return removeZeroSum(head,0)