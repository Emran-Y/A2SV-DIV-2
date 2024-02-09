class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sum = [nums[0]]
        for i in range(1,len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        answer = []
        tot = sum(nums)
        max_idx = len(nums) - 1
        for i in range(len(nums)):
            answer.append(
                (abs(((i + 1) * nums[i]) - prefix_sum[i]))
                +
                (abs(((max_idx - i) * nums[i]) - (tot - prefix_sum[i])))
            )

        return answer