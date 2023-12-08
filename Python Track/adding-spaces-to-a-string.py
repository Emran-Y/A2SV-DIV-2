class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        text = ''

        k = 0
        for i in spaces:
            text+=s[k:i] + ' '
            k = i
        return text + s[k:]
