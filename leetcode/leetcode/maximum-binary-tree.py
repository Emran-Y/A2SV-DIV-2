# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0 :
            return None
        maxNum = 0
        maxiNumInd = 0
        for i in range(len(nums)):
            if nums[i] > maxNum:
                maxNum = nums[i]
                maxiNumInd = i
        
        root = TreeNode(maxNum)
        root.left = self.helper(nums, 0, maxiNumInd - 1) #inclusive
        root.right = self.helper(nums, maxiNumInd + 1, len(nums) - 1) #inclusive
        return root

    def helper(self, nums: List[int], fromInd: int, toInd: int) -> Optional[TreeNode]:
        if fromInd > toInd: #this condition is important
            return None

        maxNum = -1  
        maxiNumInd = 0
        for i in range(fromInd, toInd + 1):
            if nums[i] > maxNum:
                maxNum = nums[i]
                maxiNumInd = i
        curr = TreeNode(maxNum)
        curr.left = self.helper(nums, fromInd, maxiNumInd - 1)
        curr.right = self.helper(nums, maxiNumInd + 1, toInd)
        return curr

        