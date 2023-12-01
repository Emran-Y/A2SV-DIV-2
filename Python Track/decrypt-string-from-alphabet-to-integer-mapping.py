class Solution:
    def freqAlphabets(self, s: str) -> str:
        hashTable = {
  '1': 'a',
  '2': 'b',
  '3': 'c',
  '4': 'd',
  '5': 'e',
  '6': 'f',
  '7': 'g',
  '8': 'h',
  '9': 'i',
  '10#': 'j',
  '11#': 'k',
  '12#': 'l',
  '13#': 'm',
  '14#': 'n',
  '15#': 'o',
  '16#': 'p',
  '17#': 'q',
  '18#': 'r',
  '19#': 's',
  '20#': 't',
  '21#': 'u',
  '22#': 'v',
  '23#': 'w',
  '24#': 'x',
  '25#': 'y',
  '26#': 'z'
}
        
        
        
        
        
        text = ''
        temp = ''
        for i in range(0,len(s)):
            temp+=s[i]
            if(len(temp) == 1):
                if( i + 2 < len(s) and s[i + 2] == '#'):
                    continue
                else:
                    text+=hashTable[temp]
                    temp = ''
            elif(len(temp) == 2):
                continue
            else:
                text+=hashTable[temp]
                temp = ''
        return text