# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        less_than = ListNode(-inf)
        greater_than = ListNode(-inf)

        less_head = less_than
        greater_head = greater_than

        curr = head

        while curr:
            if curr.val < x:
                less_than.next = curr
                less_than = less_than.next
            else:
                greater_than.next = curr
                greater_than = greater_than.next
            curr = curr.next
        greater_than.next = None
        less_than.next = greater_head.next

        return less_head.next
        
        
        

       
