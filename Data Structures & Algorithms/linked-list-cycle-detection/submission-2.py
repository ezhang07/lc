# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointerOne = head
        pointerTwo = head

        while pointerOne and pointerTwo:
            pointerOne = pointerOne.next
            pointerTwo = pointerTwo.next
            if pointerTwo:
                pointerTwo = pointerTwo.next
            if pointerOne and pointerTwo and pointerOne == pointerTwo:
                return True
        
        return False


