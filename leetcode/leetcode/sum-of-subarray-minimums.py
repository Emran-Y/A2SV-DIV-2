class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack = []
        res = 0

        for index,value in enumerate(arr):
            while stack and value < stack[-1][1]:
                j,m = stack.pop()
                left = j - stack[-1][0] if stack else j+1
                right = index - j

                res = (res + m * left * right)
            stack.append((index,value))
        for i in range(len(stack)):
            j,m = stack[i]
            left = j - stack[i-1][0] if i > 0 else j+1
            right = len(arr) - j
            res=(res + m * left * right)
        return res % (10**9 + 7)