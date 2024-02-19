class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in '+-/*':
                stack.append(i)
            else:
                if i == '+':
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif i == '-':
                    s1 = int(stack.pop())
                    s2 = int(stack.pop())
                    stack.append(s2 - s1)
                elif i == '*':
                    stack.append(int(stack.pop()) * int(stack.pop()))
                else:
                    s1 = int(stack.pop())
                    s2 = int(stack.pop())
                    stack.append(s2 / s1)
        return int(stack[0])