# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # create dummy node pointing to head
        dummy = ListNode(0, head)

        # left = dummy 
        left = dummy 
        # create right node and increment n - 1 times
        right = head

        for i in range(n - 1):
            right = right.next
        # while right.next is not None

        while right.next is not None:
                #increment left and right nodes
                left = left.next
                right = right.next

        # when right is at the end, left.next = left.next.next 
        left.next = left.next.next
        # return dummy.next 
        return dummy.next