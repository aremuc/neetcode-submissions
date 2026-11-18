# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        current = head
        temp = current.next
        current.next = None 

        while temp != None:
            next_node = temp.next
            temp.next = current
            current = temp
            temp = next_node
        
        return current

        