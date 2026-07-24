# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        fast = dummy
        for _ in range(n):
            fast = fast.next
        
        slow = dummy
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        nth = slow.next
        slow.next = nth.next
        nth.next = None

        return dummy.next
        

        