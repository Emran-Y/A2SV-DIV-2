class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
      
        window = 0
        for i in range(len(cardPoints) - k):
            window += cardPoints[i]
        tot = sum(cardPoints)
        max_ = tot - window
        l = 0
        for i in range(len(cardPoints) - k, len(cardPoints)):
            window -= cardPoints[l]
            l+=1
            window+= cardPoints[i]

            max_ = max(max_,tot - window)
        return max_