class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_window_size = 0
        temp_sum = 0
        max_sum = 0
        left = 0
        for i in nums:
            cur_window_size +=1
            temp_sum+=i
            if cur_window_size == k:
                if(max_sum == 0):
                    max_sum = temp_sum / k
                else:
                    max_sum = max(max_sum,temp_sum/k)
                temp_sum-=nums[left]
                left+=1
                cur_window_size-=1
        return max_sum
