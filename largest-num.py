class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        lst = []


        for ele in nums:
            lst += [str(ele)]
        for i in range(len(lst)):
            for j in range(i+1,len(lst)):
                if(lst[i] + lst[j] < lst[j] + lst[i]):
                    lst[i],lst[j] = lst[j],lst[i]
        return str(int(''.join(lst)))
