# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Compute the length of the list
        lenght = 0
        curr = head
        while curr:
            lenght += 1
            curr = curr.next

        # nth node to remove
        to_remove = lenght - n

        # Two pointers
        # One to iterate over to_remove
        # Second to keep one behind of the first

        dummy = ListNode()
        dummy.next = head
        first = head
        second = dummy
        i = 0
        while first:
            if i == to_remove:
                tmp = first.next
                second.next = tmp
                break
            first = first.next
            second = second.next
            i+= 1

        return dummy.next