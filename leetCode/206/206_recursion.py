# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.recursion(head)

    def recursion(self, node: ListNode, prev=None) -> ListNode:
        if not node:
            return prev
        node.next = prev
        n = node.next
        return self.recursion(n, node)
