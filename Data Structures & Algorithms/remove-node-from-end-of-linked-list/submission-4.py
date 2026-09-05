# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        
        while n > 0: # using delay to our advantage
            fast = fast.next
            n -= 1
        
        while fast and fast.next: # want to stop it 1 before on purpose. created a sliding window essentially
            slow = slow.next
            fast = fast.next # once fast.next is out of bounds, then our slow pointer is 1 before the node we need to remove


        # chance of edge case of just 1 node/ n is same len as linked list
        if not fast:
            if not slow.next: # if just 1 node in linked list, we remove the node, and return nothing
                return None
            else: # if n is same len as linked list, we're removing first element
                return slow.next

        # removing nth node, start at the node before, and get next next as temp value
        temp = slow.next.next
        slow.next.next = None # remove the next arrow from node we are removing
        slow.next = temp # make the arrow go into the next next.

        return head