class Solution:
    ##### power by chatGPT #####
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Find the node before the sublist to be removed
        prev_a = self.get_node_at_index(list1, a - 1)
        
        # Find the node after the sublist to be removed
        next_b = self.get_node_at_index(prev_a, b - a + 2)
        
        # Connect the last node of list2 to the next_b node
        last_node_list2 = self.get_last_node(list2)
        last_node_list2.next = next_b
        
        # Connect the prev_a node to the head of list2
        prev_a.next = list2
        
        return list1
    

    def get_node_at_index(self, head: ListNode, index: int) -> ListNode:
        current = head
        for _ in range(index):
            current = current.next
        return current
    
    
    def get_last_node(self, head: ListNode) -> ListNode:
        current = head
        while current.next:
            current = current.next
        return current
