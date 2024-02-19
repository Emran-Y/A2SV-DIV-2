from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque()

        for i in range(len(deck)):
            queue.append(i)

        right_ordering_of_deck = [0] * len(deck)

        for i in range(len(deck)):
            right_ordering_of_deck[queue.popleft()] = deck[i]
            if queue:queue.append(queue.popleft())
            
        return right_ordering_of_deck
        