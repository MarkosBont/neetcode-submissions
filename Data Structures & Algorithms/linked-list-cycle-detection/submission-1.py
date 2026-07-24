# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        current = head
        seen.add(current)

        while current:
            nxt = current.next
            if nxt and nxt in seen:
                return True
            
            current = nxt
            seen.add(current)
        
        return False

        