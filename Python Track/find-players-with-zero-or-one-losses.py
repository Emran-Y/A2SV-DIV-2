class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = {}
        loser = {}

        for i in matches:
            winner[i[0]] = 1
            if(i[1] in loser):
                loser[i[1]] = 0
            else:
                loser[i[1]] = 1
            if(i[1] in winner):
                winner[i[1]] = 0
            if(i[0] in loser):
                winner[i[0]] = 0
        win = []
        los = []

        for key,value in winner.items():
            if(value == 1):
                win.append(key)
        for key,value in loser.items():
            if(value == 1):
                los.append(key)
        return [sorted(win),sorted(los)]
