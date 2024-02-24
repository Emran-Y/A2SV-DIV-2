class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        maximum = float('-inf')

        for num in reversed(nums):
            if num < maximum:
                return True

            while stack and num > stack[-1]:
                maximum = stack.pop()

            stack.append(num)

        return False