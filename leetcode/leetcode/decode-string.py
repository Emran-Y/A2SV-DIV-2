class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        number = {'0','1', '2', '3', '4', '5', '6', '7', '8', '9'}
        text = ''

        for i in s:
            if i == ']':
                while stack and stack[-1] != '[':
                    text = stack.pop() + text
                stack.pop()

                num = ''
                while stack and stack[-1] in number:
                    num = stack.pop() + num

                stack.append(int(num) * text)
                text = ''
            else:
                stack.append(i)

        return ''.join(stack)