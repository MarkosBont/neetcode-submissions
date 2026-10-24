# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output = []
        print(list1)

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    output.append(list1)
                    list1 = list1.next
                
                else:
                    output.append(list2)
                    list2 = list2.next
            
            elif list1:
                output.append(list1)
                list1 = list1.next
            
            else:
                output.append(list2)
                list2 = list2.next
        
        return output

        