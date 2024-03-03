# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        store_1 = set()

        curr_1 = headA

        while curr_1:
            store_1.add(curr_1)
            curr_1 = curr_1.next

        curr_2 = headB

        while curr_2:
            if curr_2 in store_1:
                return curr_2
            curr_2 = curr_2.next