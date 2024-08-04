# 143. Reorder List

from typing import Optional
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        dummy = head
        while dummy:
            q.append(dummy.val)
            dummy = dummy.next

        dummy = head
        while q:
            dummy.val = q.popleft()
            dummy = dummy.next
            if q:
                dummy.val = q.pop()
                dummy = dummy.next
