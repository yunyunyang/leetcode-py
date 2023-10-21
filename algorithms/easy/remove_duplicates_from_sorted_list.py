# 83. Remove Duplicates from Sorted List

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head

        while dummy and dummy.next:
            if dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next

        return head


head = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2)))
sol = Solution().deleteDuplicates(head)

while sol:
    print(sol.val)
    sol = sol.next
