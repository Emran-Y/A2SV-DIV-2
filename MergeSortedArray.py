class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if(m == 0):
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return
        p1 = m - 1
        p2 = n - 1
        p = n + m - 1
        while(p1 >= 0 and p2 >= 0):
            if(nums2[p2] > nums1[p1]):
                nums1[p] = nums2[p2]
                p2-=1
                p-=1
            else:
                nums1[p] = nums1[p1]
                p1-=1
                p-=1
        while(p1 >= 0):
            nums1[p] = nums1[p1]
            p1-=1
            p-=1
        while(p2 >= 0):
            nums1[p] = nums2[p2]
            p2-=1
            p-=1
        
        
