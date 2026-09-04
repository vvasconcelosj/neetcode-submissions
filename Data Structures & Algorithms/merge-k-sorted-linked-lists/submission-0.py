# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge_lists(self, list_a: ListNode, list_b: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        while list_a and list_b:
            if list_a.val < list_b.val:
                curr.next = list_a
                list_a = list_a.next
            else:
                curr.next = list_b
                list_b = list_b.next

            curr = curr.next

        curr.next = list_a or list_b

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) >= 2:
            a = lists.pop()
            b = lists.pop()

            c = self.merge_lists(a, b)

            lists.append(c)

        return lists[0]
