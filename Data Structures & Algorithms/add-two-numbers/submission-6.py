# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        recent = dummy

        while l1 or l2 or carry > 0:
            if l1 and l2:
                add = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                add = l1.val + carry
                l1 = l1.next
            elif l2:
                add = l2.val + carry
                l2 = l2.next
            else:
                add = carry

            carry = add // 10
            final_add = add % 10
            recent.next = ListNode(final_add)
            recent = recent.next

        return dummy.next



        