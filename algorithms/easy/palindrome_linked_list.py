# 234. Palindrome Linked List

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        while head:
            l.append(head.val)
            head = head.next

        return l == l[::-1]

# head = [1,2,2,1]
head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=2, next=ListNode(val=1))))
# head = ListNode(val=1, next=ListNode(val=2))
sol = Solution().isPalindrome(head)
print(sol)    