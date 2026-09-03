# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle of the list
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Break the list
        second = slow.next
        slow.next = None

        # Reverse 2nd half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge lists 
        # The second will be shortest always due partition 
        
        second = prev
        first = head
        while second:
            tmp_first, tmp_second = first.next, second.next

            first.next = second
            second.next = tmp_first

            first = tmp_first
            second = tmp_second