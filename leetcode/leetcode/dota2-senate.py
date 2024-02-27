from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        for i, party in enumerate(senate):
            if party == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            radiant_index = radiant.popleft()
            dire_index = dire.popleft()

            if radiant_index < dire_index:
                radiant.append(radiant_index + len(senate))
            else:
                dire.append(dire_index + len(senate))

        return "Radiant" if radiant else "Dire"