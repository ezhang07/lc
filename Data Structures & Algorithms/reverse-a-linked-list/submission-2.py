# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head # so we not changing the copy of the input ??
        prev = None # how we will reverse

        while curr: # traversing linked list
            temp = curr.next # so we can traverse linked list
            curr.next = prev # change the arrow to be looking at previous node
            prev = curr # part of traversing to new val, we increment prev position
            curr = temp # we increment curr position, so basically shifted prev and curr by 1
        
        return prev # the prev becomes the new head, since we reversed it