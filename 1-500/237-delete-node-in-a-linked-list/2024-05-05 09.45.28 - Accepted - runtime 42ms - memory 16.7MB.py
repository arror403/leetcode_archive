# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        nextNode = node.next
        node.val = node.next.val
        node.next = nextNode.next
        nextNode.next = None