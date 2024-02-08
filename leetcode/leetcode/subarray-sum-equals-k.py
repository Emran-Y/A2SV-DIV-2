class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = {0:1}
        count = 0

        sum_ = 0
        for i in nums:
            sum_+=i
            if(sum_ - k in table):
                count+=table[sum_ - k]
                table[sum_] = 1 + table.get(sum_,0)
            else:
                table[sum_] = 1 + table.get(sum_,0)
        return count

