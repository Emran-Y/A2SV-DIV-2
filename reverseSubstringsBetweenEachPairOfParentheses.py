class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in '+/*-':
                stack.append(i)
            else:
                one = int(stack.pop())
                two = int(stack.pop())
                if i == '+':
                    val = two + one
                elif i == '-':
                    val = two - one
                elif i == '*':
                    val = two * one
                else:
                    val = int(two / one)
                stack.append(val)
        return int(stack[0])
