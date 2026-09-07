# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head # slow fast pointer approach

        if fast and fast.next: # for edge case where there's 2 nodes in linked list, no cycle.
            fast = fast.next # doesn't affect other scenarios
        
        while fast and fast.next: # ensure that fast and fast.next are non-null
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False