class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first number
                
            L = i + 1
            R = len(nums) - 1
            
            while L < R:
                total = nums[i] + nums[L] + nums[R]
                if total < 0:
                    L += 1
                elif total > 0:
                    R -= 1
                else:
                    answer.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1  # Skip duplicates for the second number
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1  # Skip duplicates for the third number
                    L += 1
                    R -= 1

        return answer