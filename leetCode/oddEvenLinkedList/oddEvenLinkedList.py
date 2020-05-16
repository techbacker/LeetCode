# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(self, head: ListNode) -> ListNode:
    no_of_nodes = 0
    last = None
    temp = head
    while(temp!=None):
        no_of_nodes += 1
        last = temp
        temp = temp.next
    temp = head
    while(no_of_nodes > 1):
        if temp!= None and temp.next!=None:
            last.next = temp.next
            last = last.next
            temp.next = temp.next.next
            temp = temp.next
            last.next = None
            no_of_nodes -= 2
    return head
