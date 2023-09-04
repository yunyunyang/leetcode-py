# 141. Linked List Cycle

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True

        return False

    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     d = set()
    #     while head:
    #         if head in d:
    #             return True
    #         if not head.next:
    #             return False

    #         d.add(head)
    #         head = head.next


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
sol = Solution().hasCycle(head)
print(sol)
