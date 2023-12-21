class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c = 0

        for i in range(len(strs[0])):
            temp = ''
            for j in range(len(strs)):
                temp+=strs[j][i]
            if(temp != ''.join(sorted(temp))):
                c+=1
        return c



