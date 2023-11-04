class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        P = []

        for i in range(len(nums)):
            if(i==0):
                P.append(nums[0])
            else:
                P.append(P[i-1] * nums[i])
        S = [0] * len(nums)
        R = len(nums) - 1
        for i in range(len(nums) - 1,-1,-1):
            if(i==len(nums) - 1):
                S[R] = nums[i]
                R-=1
            else:
                S[R] = S[i+1] * nums[i]
                R-=1
        Final = []
        for i in range(len(nums)):
            if(i-1 >= 0 and i+1 < len(nums)):
                Final.append(P[i-1] * S[i+1])
            elif(i-1 >= 0):
                Final.append(P[i-1])
            elif(i+1 < len(nums)):
                Final.append(S[i+1])
        return Final
