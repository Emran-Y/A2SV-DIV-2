class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        stack = []

        for i in s:
            if(len(stack) == 0):
                stack.append(dict[i])
            else:
                if stack[-1] >= dict[i]:
                    stack.append(dict[i])
                else:
                    stack.append(dict[i] - stack.pop())
        return sum(stack)
                