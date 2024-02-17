class Solution:
    def numberOfWays(self, s: str) -> int:
        before_zeros = 0
        before_ones = 0
        ways = 0
        all_ones = s.count('1')
        all_zeros = s.count('0')

        for i in range(len(s)):
            if i == 0:
                if s[i] == '0':before_zeros+=1
                else:before_ones+=1
                continue
            if s[i] == '1':
                ways+= before_zeros * (all_zeros - before_zeros)
                before_ones+=1
            else:
                ways+= before_ones * (all_ones - before_ones)
                before_zeros+=1
        return ways

