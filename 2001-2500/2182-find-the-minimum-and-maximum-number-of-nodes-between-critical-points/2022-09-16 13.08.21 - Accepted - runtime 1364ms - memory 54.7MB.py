# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        m=self.LinkedToArr(head)
        
        
        def isCriticalPoint(prev,  pres, next):

            # Critical point condition
            if ((prev < pres and pres > next)
                    or (prev > pres and pres < next)):
                return True
            return False

        # Function to find the required distances
        def maxmincriticaldis(arr,  n):

            # Store the position
            pos = []

            # Start from index 1 as we are gonna pass
            # arr[i-1] and at i=0 i-1 becomes -ve
            # to avoid that error we start from index 1
            for i in range(1, n - 1):

                # If this point is critical point then it's
                # index is inserted in the pos array
                if (isCriticalPoint(arr[i - 1], arr[i],
                                    arr[i + 1])):
                    pos.append(i)

            ans = []

            # If the pos array size is either 0 or 1
            # then we will simply add -1 and -1 to the answer array
            # as it is not possible to find the max and min
            # distance with 1 or 0 elements in the array.
            if (len(pos) <= 1):
                ans.append(-1)
                ans.append(-1)

            else:

                # We find the minimum difference between the
                # positions of the critical points based on the
                # values of indexes.
                mval = sys.maxsize
                for i in range(1, len(pos)):
                    mval = min(mval, pos[i] - pos[i - 1])
                ans.append(mval)

                # Maximum difference will obviously be between
                # the first and the last element of the pos array.
                ans.append(pos[len(pos) - 1] - pos[0])

            return ans
        
        return maxmincriticaldis(m,len(m))
        
        
    def LinkedToArr(self, head):
        arr = []
        curr = head
        while (curr != None): 
            arr.append(curr.val)
            curr = curr.next
        return arr