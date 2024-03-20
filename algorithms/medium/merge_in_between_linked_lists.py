# 1669. Merge In Between Linked Lists

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = list1
        for _ in range(a - 1):
            dummy = dummy.next

        detach = dummy.next
        for _ in range(b - a + 1):
            detach = detach.next

        dummy.next = list2
        while list2.next:
            list2 = list2.next
        
        list2.next = detach

        return list1


list1 = ListNode(val=10, next=ListNode(val=1, next=ListNode(
    val=13, next=ListNode(val=6, next=ListNode(val=9, next=ListNode(val=5))))))
list2 = ListNode(val=1000000, next=ListNode(
    val=1000001, next=ListNode(val=1000002)))
sol = Solution().mergeInBetween(list1=list1, a=3, b=4, list2=list2)

while sol:
    print(sol.val)
    sol = sol.next
