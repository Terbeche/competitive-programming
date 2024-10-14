from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next

        arr.sort()
      
        dummy = ListNode(0)
        current = dummy
        
        for val in arr:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next