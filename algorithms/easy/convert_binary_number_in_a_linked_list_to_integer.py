# 1290. Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        output = 0
        nodes = []
        while head is not None:
            nodes.append(head.val)
            head = head.next

        nodes.reverse()
        for i, n in enumerate(nodes):
            if n == 1:
                output += 2 ** i

        return output

sol = Solution().getDecimalValue(head = ListNode(val=1, next=ListNode(val=0, next=ListNode(val=1))))
print(sol)