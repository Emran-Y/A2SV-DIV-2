# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummyNode = ListNode(1)
        dummyNode.next =  head

        curr_1 =dummyNode
        curr_2 = dummyNode

        for i in range(n):
            curr_1 = curr_1.next
        while curr_1 and curr_1.next:
            curr_1 = curr_1.next
            curr_2 = curr_2.next
        if ( curr_1 ):
            curr_2.next = curr_2.next.next
        else:
            dummyNode.next = head.next
        return dummyNode.next