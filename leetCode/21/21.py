# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        # base case
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next

        head.next = self.mergeTwoLists(l1, l2)
        return head