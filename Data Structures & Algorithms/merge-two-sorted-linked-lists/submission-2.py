# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        curr aproach:
        look at both the sorted lists, compare values of nodes
        l1.val > l2.val -> l2 node is added to res, and then l2 = l2.next.
        might use dummy for res. if lists are diff lengtt, at end need to check for whether one is non-empty
        while list1 and list2:
        """

        res = ListNode() # initialized with a blank node, needed for dummy later
        dummy = res # since we want to return at the head of the linked list that merged both, thius will help

        while list1 and list2: # while both lists are non empty, we can continue traversing them
            if list1.val > list2.val: # list2 value smaller, so we add it to the res
                res.next = list2
                res = res.next # make sure we're shifting the node we're looking at
                list2 = list2.next
            else:
                res.next = list1
                res = res.next
                list1 = list1.next
        
        if list1: # if lists have diff lengths, one of them could be non-empty still, so then we just add the remainder of their lists
            res.next = list1
        if list2:
            res.next = list2
        
        return dummy.next