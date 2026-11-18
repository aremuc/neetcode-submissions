# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # edge case
        if head is None:
            return False
        
        # slow pointer at head
        slow = head

        # fast pointer at head
        fast = head

        # while fast moves, slow moves 1, fast moves 2
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # if slow is fast, return true
            if slow is fast:
                return True

        # return false, fast eventually reaches None
        return False

