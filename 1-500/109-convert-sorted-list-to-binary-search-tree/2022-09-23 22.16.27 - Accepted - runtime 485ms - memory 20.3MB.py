# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        m=self.LinkedToArr(head)
        return self.sortedArrayToBST(m)
    
    
    def sortedArrayToBST(self, arr):
        if not arr:
            return None
        # find middle index
        mid = (len(arr)) // 2
        # make the middle element the root
        root = TreeNode(arr[mid])
        # left subtree of root has all
        # values <arr[mid]
        root.left = self.sortedArrayToBST(arr[:mid])
        # right subtree of root has all
        # values >arr[mid]
        root.right = self.sortedArrayToBST(arr[mid+1:])
        return root

        
    def LinkedToArr(self, head):
        arr = []
        curr = head
        while (curr != None): 
            arr.append(curr.val)
            curr = curr.next
        return arr