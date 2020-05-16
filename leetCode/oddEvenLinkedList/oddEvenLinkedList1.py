# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(self, head: ListNode) -> ListNode:
    odd = head
    if head is not None:
        even = head.next
        evenHead = even
        while (even is not None and even.next is not None):
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next
        if evenHead is not None:
            odd.next = evenHead
    return head
