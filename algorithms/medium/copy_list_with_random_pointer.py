# 138. Copy List with Random Pointer

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_copy = {None: None}
        dummy = head
        while dummy:
            node = Node(dummy.val)
            old_copy[dummy] = node
            dummy = dummy.next

        dummy = head
        while dummy:
            copy = old_copy[dummy]
            copy.next = old_copy[dummy.next]
            copy.random = old_copy[dummy.random]
            dummy = dummy.next

        return old_copy[head]