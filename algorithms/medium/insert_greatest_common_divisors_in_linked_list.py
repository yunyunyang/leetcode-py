# 2807. Insert Greatest Common Divisors in Linked List

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        while head:
            node = head.next
            if node:
                if head.val >= head.next.val:
                    n, m = head.val, head.next.val
                else:
                    n, m = head.next.val, head.val

                gcd = self.gcd(n, m)
                head.next = ListNode(val=gcd, next=head.next)
            head = node

        return root
    
    def gcd(self, n, m):
        if m == 0:
            return n
        else:
            return self.gcd(m, n%m)

head = ListNode(val=18, next=ListNode(val=6, next=ListNode(val=10, next=ListNode(val=3))))
sol = Solution().insertGreatestCommonDivisors(head)

while sol:
    print(sol.val)
    sol = sol.next