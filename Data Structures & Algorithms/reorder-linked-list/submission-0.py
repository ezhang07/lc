# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        secondHalf = slow.next
        slow.next = None
        prev = None
        while secondHalf:
            nextVal = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = nextVal
        

        secondHalf = prev
        firstHalf = head
        while secondHalf:
            temp1 = firstHalf.next
            temp2 = secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            firstHalf = temp1
            secondHalf = temp2






        


        



