# Problem: Find Xor-Beauty of Array - https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution:
    def xorBeauty(self, nums: list[int]) -> int:
        beauty = 0
        max_num = max(nums)
        max_bit = 0
        
        while (1 << max_bit) <= max_num:
            max_bit += 1
        
        for bit in range(max_bit):
            cnt = [0, 0]
            for num in nums:
                cnt[(num >> bit) & 1] += 1
            
            for i in (0, 1):
                for j in (0, 1):
                    for k in (0, 1):
                        if (cnt[i] * cnt[j] * cnt[k]) & 1:
                            beauty ^= ((i | j) & k) << bit
        
        return beauty
