# 2181. Merge Nodes in Between Zeros

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = None
        sum = 0
        while head:
            sum += head.val
            if head.val == 0:
                if tmp == None:
                    print(f'head={sum}')
                    tmp = output = ListNode(val=sum)
                else:
                    print(f'node={sum}')
                    tmp.next = ListNode(val=sum)
                    tmp = tmp.next

                sum = 0
            head = head.next

        return output.next


sol = Solution().mergeNodes(head = 
ListNode(val=0, next=
ListNode(val=3, next=
ListNode(val=1, next=
ListNode(val=0, next=
ListNode(val=4, next=
ListNode(val=5, next=
ListNode(val=2, next=
ListNode(val=0)))))))))

# ListNode(val=0, next=
# ListNode(val=1, next=
# ListNode(val=0, next=
# ListNode(val=3, next=
# ListNode(val=0, next=
# ListNode(val=2, next=
# ListNode(val=2, next=
# ListNode(val=0)))))))))
