class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for curr_char in s:
            if stack and stack[-1] == '(':
                if curr_char == ')':
                    stack.pop()
                else:
                    stack.append(curr_char)
            else:
                stack.append(curr_char)
        return len(stack)