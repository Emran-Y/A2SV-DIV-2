class Solution:
    def isValid(self, s: str) -> bool:
        if(s[0] in '}])'):
            return False
        hashTable = {')':'(',']':'[','}':'{'}
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if stack and stack[-1] == hashTable[i]:
                    stack.pop()
                else:
                    return False
        return True if stack == [] else False