class Solution:
    def longestPalindrome(self, s: str) -> int:
        table = {}

        for i in s:
            table[i] = 1 + table.get(i,0)
        length_of_the_longest_palindrome = 0
        odd_visited = False

        for i in table:
            if table[i]%2==0:
                length_of_the_longest_palindrome+=table[i]
            else:
                if not odd_visited:
                    if table[i] == 1:
                        length_of_the_longest_palindrome+=1
                        odd_visited = True
                    else:
                        length_of_the_longest_palindrome+=table[i]
                        odd_visited = True
                else:
                    if table[i] != 1:
                        length_of_the_longest_palindrome+=table[i]-1
        return length_of_the_longest_palindrome
        