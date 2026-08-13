# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        # Finding the middle of linked list
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        

        second = slow.next
        slow.next = None

        # Reversing 2nd array
        curr = second
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Merging the two lists
        dummy = ListNode()
        curr = dummy

        curr1 = head
        curr2 = prev

        while curr1:
            curr.next = curr1
            curr1 = curr1.next
            curr = curr.next

            if curr2:
                curr.next = curr2
                curr2 = curr2.next
                curr = curr.next


