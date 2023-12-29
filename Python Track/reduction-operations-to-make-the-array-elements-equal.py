class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        op = 0

        dict = {}
        for i in nums:
            dict[i] = 1 + dict.get(i,0)
        hash = list(set(nums))
        hash.sort(reverse=True)

        for i in range(len(hash)):
            if(len(dict) == 1):
                break
            op+=dict[hash[i]]
            if(i + 1 < len(hash)):
                dict[hash[i+1]] +=  dict[hash[i]]
            del dict[hash[i]]

        return op

        