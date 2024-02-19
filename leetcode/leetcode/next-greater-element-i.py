class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ourdict = {}
        for i,n in enumerate(nums1):
            ourdict[n] = i
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                index = ourdict[val]
                res[index] = cur
            if(cur in nums1):
                stack.append(cur)
        return res
        