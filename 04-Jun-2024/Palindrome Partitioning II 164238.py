# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for length in range(len(s)):
            for start in range(len(s)-length):
                if length == 0 or (s[start] == s[start+length] and (dp[start+1][start+1+length-2] or length == 1)):
                    dp[start][start+length] = 1
                else:
                    dp[start][start+length] = 0

        @functools.cache
        def minPalindrome(prevCut):
            if prevCut == len(s):
                return 0
            cut = math.inf
            for x in range(prevCut, len(s)):
                if dp[prevCut][x]:
                    cut = min(cut, minPalindrome(x+1))
            return cut+1
        return minPalindrome(0)-1
        