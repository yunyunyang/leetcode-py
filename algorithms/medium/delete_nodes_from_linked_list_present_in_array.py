# 3217. Delete Nodes From Linked List Present in Array

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode()
        curr = dummy

        while head:
            if head.val not in nums:
                curr.next = head
                curr = curr.next
            head = head.next

        curr.next = None
        return dummy.next