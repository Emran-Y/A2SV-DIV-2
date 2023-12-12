class Solution:
    def twoSum(self, nums, target):
        flag = []
        list_length = len(nums)
        for i in range(list_length - 1):
            for j in range(i + 1,list_length):
                if nums[i] + nums[j] == target:
                    flag = [i,j]
                else:
                    continue 
        return flag


