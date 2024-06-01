# 148. Sort List

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
            
        nums.sort()
        output = dummy = ListNode()
        for n in nums:
            dummy.next = ListNode(n)
            dummy = dummy.next
            
        return output.next