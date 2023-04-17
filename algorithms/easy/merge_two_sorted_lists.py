# 21. Merge Two Sorted Lists

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        o = t = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                t.next = list1
                list1 = list1.next
            else:
                t.next = list2
                list2 = list2.next
            t = t.next

        t.next = list1 or list2
        return o.next

list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4)))
list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))
sol = Solution().mergeTwoLists(list1, list2)

while sol:
    print(sol.val)
    sol = sol.next