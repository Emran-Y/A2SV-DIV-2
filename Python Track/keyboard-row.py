class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        letter_dict = {
    'q': '1',
    'w': '1',
    'e': '1',
    'r': '1',
    't': '1',
    'p':'1',
    'y': '1',
    'u': '1',
    'i': '1',
    'o': '1',
    'a': '2',
    's': '2',
    'd': '2',
    'f': '2',
    'g': '2',
    'h': '2',
    'j': '2',
    'k': '2',
    'l': '2',
    'z': '3',
    'x': '3',
    'c': '3',
    'v': '3',
    'b': '3',
    'n': '3',
    'm': '3'
}

        final = []
        
        for i in words:
            temp = ''

            for j in i:
                temp+=letter_dict[j.lower()]
            if(temp == '1' * len(i) or temp == '2' * len(i) or temp == '3' * len(i) ):
                final.append(i)
            temp = ''
        return final
