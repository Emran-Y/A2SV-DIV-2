class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                index =  stack.pop()

                ans[index] = nums[i]
            stack.append(i)
        
        for i in range(len(nums)):
            if not stack:
                break
            while nums[stack[-1]] < nums[i]:
                index = stack.pop()
                ans[index] = nums[i]
        return ans