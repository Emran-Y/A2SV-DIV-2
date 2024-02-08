class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]):
        prefix = [0] * len(s)

        for i in shifts:
            if i[2] == 1:
                prefix[i[0]] += 1
                if(i[1] + 1 < len(s)):
                    prefix[i[1] + 1] -= 1
            else:
                prefix[i[0]] -= 1
                if(i[1] + 1 < len(s)):
                    prefix[i[1] + 1] += 1
        sum_ = [prefix[0]]
        acc = prefix[0]

        for i in range(1,len(prefix)):
            acc+=prefix[i]
            sum_.append(acc)
        ans = ''
        print(sum_)
        for i in range(len(s)):
            if(97 <= ord(s[i]) + sum_[i] <= 122):
                ans+=chr(ord(s[i]) + sum_[i])
            else:
                if(ord(s[i]) + sum_[i] < 97):
                    ans+=chr(122 - ((96 - (ord(s[i]) + sum_[i]) ) %26))
                else:

                    ans+=chr(97 + (((ord(s[i]) + sum_[i]) - 123)%26)  )
        return ans

        

