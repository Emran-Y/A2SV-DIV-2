# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if not cur.children[ord(char) - ord('a')]:
                new_trie = TrieNode()
                cur.children[ord(char) - ord('a')] = new_trie
                cur = new_trie
            else:
                cur = cur.children[ord(char) - ord('a')]
        cur.is_end = True
    
    def all(self) -> list:
        ans = []
        
        def dfs(node, temp):
            exhausted_path = True
            for i in range(26):
                if node.children[i] is not None:
                    new_temp = temp + chr(97 + i)
                    dfs(node.children[i], new_temp)
                    exhausted_path = False
            if exhausted_path:
                ans.append(temp)
            
        dfs(self.root, '')
        return ans

class Solution:
    def longestWord(self, words: List[str]) -> str:
        my_trie = Trie()
        for word in words:
            my_trie.insert(word)
        possible_words = my_trie.all()
        ans = ''
        ans_len = 0

        for word in possible_words:
            is_candidate = True
            for i in range(1, len(word)):
                if word[:i] not in words:
                    is_candidate = False
                    break
                else:
                    if len(word[:i]) > ans_len:
                        ans = word[:i]
                        ans_len = len(word[:i])
            if is_candidate and len(word) > ans_len:
                ans = word
                ans_len = len(word)
        
        return ans