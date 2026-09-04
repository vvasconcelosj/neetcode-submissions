# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time: O(list_a + list_b)
    # Space: O(1)     
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

    # Time: O(n * log lists)
    # Space: O(1)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                a = lists[i]
                b = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.merge_lists(a, b))

            lists = merged
        return lists[0]