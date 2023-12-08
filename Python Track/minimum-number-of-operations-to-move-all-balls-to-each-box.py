class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        indx = []

        for i in range(len(boxes)):
            if(boxes[i] != '0'):
                indx.append(i)
        ans = []

        for i in range(len(boxes)):

            temp = 0

            for j in indx:
                if(i == j):
                    continue
                else:
                    temp+= abs(i-j)
            ans.append(temp)
        return ans
