class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        


        tasks.sort()
        processorTime.sort(reverse = True)

        k = 0
        max_ = 0

        for i in range( len(tasks) // 4 ):
            max_ = max(max_,processorTime[k] + tasks[(4 * (k + 1)) - 1])
            k+=1
        return max_