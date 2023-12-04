class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True 
        hashTable = {}
        tracker = 0
        for i in order:
            hashTable[i] = tracker
            tracker += 1
        L = 0
        R = 1
        while R < len(words):
            if hashTable[words[L][0]] < hashTable[words[R][0]]:
                L += 1
                R += 1
            elif hashTable[words[L][0]] > hashTable[words[R][0]]:
                return False
            else:
                l = 1
                r = 1
                while l < len(words[L]) and r < len(words[R]):
                    if hashTable[words[L][l]] < hashTable[words[R][r]]:
                        break
                    elif hashTable[words[L][l]] > hashTable[words[R][r]]:
                        return False
                    else:
                        l += 1
                        r += 1
                if(l < len(words[L])) and( r >= len(words[R])):
                    return False
                
                L+=1
                R+=1
        return True