class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}

        if(len(nums1) > len(nums2)):
            for i in nums1:
                dict[i] = 1 + dict.get(i,0)
            ans = []
            for i in nums2:
                if i in dict:
                    ans.append(i)
                    dict[i] = dict.get(i) - 1
                    if(dict[i] == 0):
                        del dict[i]
            return ans
        else:
            for i in nums2:
                dict[i] = 1 + dict.get(i,0)
            ans = []
            for i in nums1:
                if i in dict:
                    ans.append(i)
                    dict[i] = dict.get(i) - 1
                    if(dict[i] == 0):
                        del dict[i]
            return ans