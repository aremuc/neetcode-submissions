# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1. find middle

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        #   2. reverse second half
        previous = None
        current = slow.next
        slow.next = None

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        #   3. first = head

        first = head

        #   4. second = head of reversed second half
        second = previous
        #   5. while second still has nodes:

        while second is not None:
            #    save first.next
            next_front = first.next
            #    save second.next
            next_back = second.next
            #    first.next = second
            first.next = second
            #    second.next = saved first.next
            second.next = next_front
            #    first = saved first.next
            first = second.next
            second = next_back
        


