class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pre_arr = [0] * len(nums)

        for i in requests:
            pre_arr[i[0]]+=1
            if(i[1] + 1 < len(pre_arr)):
                pre_arr[i[1] + 1]-=1
        
        for i in range(1,len(pre_arr)):
            pre_arr[i] = pre_arr[i-1] + pre_arr[i]

        pre_arr.sort(reverse=True)
        nums.sort(reverse=True)

        tot = 0

        for i in range(len(nums)):
            if(pre_arr[i]!=0):
                tot+=nums[i] * pre_arr[i]
            else:
                break
        return tot%(10**9 + 7)