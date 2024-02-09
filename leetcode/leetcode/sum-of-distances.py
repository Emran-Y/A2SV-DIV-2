class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        answer = [0] * len(nums)
        
        idx_left_sum = defaultdict(int)
        num_val_left = defaultdict(int)

        for i in range(len(nums)):
            answer[i]+=num_val_left[nums[i]] * i
            answer[i]-= idx_left_sum[nums[i]]
            num_val_left[nums[i]]+=1
            idx_left_sum[nums[i]]+=i
        
        idx_right_sum = defaultdict(int)
        num_val_right = defaultdict(int)

        for i in range(len(nums) - 1 , -1 , -1 ):
            answer[i]+=idx_right_sum[nums[i]]
            answer[i]-=num_val_right[nums[i]] * i
            idx_right_sum[nums[i]]+=i
            num_val_right[nums[i]]+=1

        return answer



