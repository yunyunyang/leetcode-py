# 203. Remove Linked List Elements

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = ListNode()
        out = cur
        while head:
            n = head.next
            if head.val != val:
                cur.next = head
                cur = cur.next
                cur.next = None
            head = n

        return out.next

# head = [1,2,6,3,4,5,6], val = 6
head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=6, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=ListNode(val=6)))))))
sol = Solution().removeElements(head = head, val = 6)
print(sol)