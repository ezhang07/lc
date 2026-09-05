# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        first need to do slow fast pointer, to find middle. slow ptr will be in the middle of list.
        with that, on the 2nd part of the array we can reverse the linked list. btw we also wanna split them. 
        after that we can merge the two together.
        """

        slow = head
        fast = head

        # to find the middle of linked list. 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the linked list from slow ptr, exactly same proc as reverse linked list lc
        prev = None
        curr = slow.next
        slow.next = None # this is required so that 1st linked list is ended (not sure if this is valid)

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # prev is starting of 2nd list, now we have 2 linked lists. now we just merge
        list1 = head
        list2 = prev

        while list1 and list2: 
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1

            list1 = temp1
            list2 = temp2







        


        



