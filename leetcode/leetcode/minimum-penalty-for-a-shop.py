class Solution:
    def bestClosingTime(self, customers: str) -> int:
        arr = [0]
        totY = 0
        totN = 0
        for i in customers:
            if i == 'Y':
                arr.append(1)
                totY+=1
            else:
                arr.append(0)
                totN+=1
        for i in range(1,len(arr)):
            arr[i] = arr[i-1] + arr[i]

        tempIndex = 0
        tempPenalty = float("inf")

        for i in range(len(arr)):
            leftY = arr[i]
            leftN = (i) - arr[i]
            rightY = totY - leftY
            if tempPenalty > (leftN + rightY):
                tempIndex = i
                tempPenalty = leftN + rightY
        return tempIndex
        




