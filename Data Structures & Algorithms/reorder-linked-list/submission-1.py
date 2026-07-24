# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = None

        slow.next = None


        # reversing second half
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        # merging two halves
        first = head
        second = prev

        while second:
            nxt1 = first.next
            nxt2 = second.next

            first.next = second
            second.next= nxt1

            first = nxt1
            second = nxt2



        


        
        