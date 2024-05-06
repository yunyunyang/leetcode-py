# 2487. Remove Nodes From Linked List

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            while stack and stack[-1].val < head.val:
                stack.pop()
            stack.append(head)
            head = head.next
        
        nodes = ListNode()
        dummy = nodes
        for i in range(len(stack)):
            nodes.next = ListNode(val=stack[i].val)
            nodes = nodes.next

        return dummy.next

head = ListNode(val=5, next=ListNode(val=2, next=ListNode(val=13, next=ListNode(val=3, next=ListNode(val=8)))))   
sol = Solution().removeNodes(head)
while sol:
    print(sol.val)
    sol = sol.next
