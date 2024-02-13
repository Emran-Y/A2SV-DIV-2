# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit = head
        tort = head

        while rabbit and rabbit.next:
            rabbit = rabbit.next.next
            tort = tort.next

            if rabbit == tort:
                return True
        return False