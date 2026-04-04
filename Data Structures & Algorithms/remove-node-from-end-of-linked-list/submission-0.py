# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0

        while curr:
            length+=1
            curr = curr.next

        indexToRemove = length - n
        count = 0

        removePass = head
        prev = None

        while removePass:
            if count == indexToRemove:
                if not prev:
                    return head.next
                prev.next = removePass.next
                break
                
                
                
            else:
                prev = removePass
                removePass = removePass.next

            count+=1
        
        return head
            
        


            

            