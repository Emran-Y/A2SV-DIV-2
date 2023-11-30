class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        s = ''

        for i in command:
            if(i=='G'):
                s+='G'
            elif(i=='('):
                stack.append(i)
            elif(i==')'):
                if(stack.pop() == 'l'):
                    s+='al'
                else:
                    s+='o'
            else:
                stack.append(i)
        return s