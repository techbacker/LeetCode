# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
      if not head or not head.next:
            return head
      first = head.next
      second = head
      second.next = self.swapPairs(first.next)
      first.next = second
      return first

firstNode = ListNode()
secondNode = ListNode()
thirdNode = ListNode()
forthNode = ListNode()
firstNode.val = 1
secondNode.val = 2
thirdNode.val = 3
forthNode.val = 4
firstNode.next = secondNode
secondNode.next = thirdNode
thirdNode.next = forthNode
forthNode.next = None
res = Solution().swapPairs(firstNode)
print(res.val)