# 2816. Double a Number Represented as a Linked List

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the linked list
        reversed_list = self.reverseList(head)

        # Initialize variables to track carry and previous node
        carry = 0
        previous, current = None, reversed_list

        # Traverse the reversed linked list
        while current:
            # Calculate the new value for the current node
            new_val = current.val * 2 + carry
            # Update the current node's value
            current.val = new_val % 10
            # Update carry for the next iteration
            carry = 1 if new_val > 9 else 0
            # Move to the next node
            previous, current = current, current.next

        # If there's a carry after the loop, add an extra node
        if carry:
            previous.next = ListNode(val=carry)

        # Reverse the list again to get the original order
        output = self.reverseList(reversed_list)

        return output
    
    # Method to reverse the linked list
    def reverseList(self, node: ListNode) -> ListNode:
        previous, current = None, node

        # Traverse the original linked list
        while current:
            # Store the next node
            next_node = current.next
            # Reverse the link
            current.next = previous
            # Move to the next nodes
            previous, current = current, next_node

        # Previous becomes the new head of the reversed list
        return previous


head = ListNode(val=1, next=ListNode(val=8, next=ListNode(val=9)))
sol = Solution().doubleIt(head)
while sol:
    print(sol.val)
    sol = sol.next