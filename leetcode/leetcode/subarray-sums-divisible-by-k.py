class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        table = {0:1}
        count = 0

        sum_ = 0

        for i in nums:
            sum_+=i
            if(sum_%k in table):
                count+=table[sum_%k]
                table[sum_%k]+=1
            else:
                table[sum_%k]  = 1 + table.get(sum_%k,0)
        return count