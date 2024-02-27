class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(idx,cur):
            if idx >= len(num):
                return len(cur) >= 3
            for i in range(idx,len(num)):
                tempString = num[idx:i+1]
                if len(tempString) > 1 and tempString[0] == '0':
                    continue
                temp = int(num[idx:i+1])
                if len(cur) < 2 or (temp == cur[-1] + cur[-2]):

                    if backtrack(i + 1,cur + [temp]):
                        return True
            return False
        return backtrack(0,[])

