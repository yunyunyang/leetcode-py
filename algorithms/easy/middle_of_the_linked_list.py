# 876. Middle of the Linked List

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size, dummy = 0, head
        while dummy:
            size += 1
            dummy = dummy.next

        idx, middle = 0, size // 2 + 1
        print(middle)
        while head:
            idx += 1
            if middle == idx:
                return head

            head = head.next


head = ListNode(val=1, next=ListNode(val=2, next=ListNode(
    val=3, next=ListNode(val=4, next=ListNode(val=5)))))
sol = Solution().middleNode(head)
print(sol)
