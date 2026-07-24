# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstNum = ""
        secNum = ""

        curr = l1
        while curr:
            firstNum += str(curr.val)
            curr = curr.next
        
        curr = l2
        while curr:
            secNum += str(curr.val)
            curr = curr.next
        
        firstNum = int(firstNum[::-1])
        secNum = int(secNum[::-1])

        final = str(firstNum + secNum)
        final = final[::-1]

        dummy = ListNode()
        recent = dummy

        for char in final:
            new = ListNode(val=int(char))
            recent.next = new
            recent = new
        
        return dummy.next
        





        