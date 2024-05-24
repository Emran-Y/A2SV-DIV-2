# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        def find_mid(head): 
            slow = head
            fast = head.next 
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def merge(left, right):
            dummy = ListNode(0)
            temp = dummy
            while left and right:
                if left.val < right.val:
                    temp.next = left
                    left = left.next
                else:
                    temp.next = right
                    right = right.next
                temp = temp.next
            temp.next = left or right
            return dummy.next
        
        def merge_sort(head):
            if not head or not head.next:
                return head
            mid = find_mid(head)
            right_head = mid.next 
            mid.next = None
            left_sorted = merge_sort(head)
            right_sorted = merge_sort(right_head)
            return merge(left_sorted, right_sorted)
        
        return merge_sort(head)
