class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        d = {}

        l = 0
        min_ = 0
        sum_w  = 0

        for R in range(len(cards)):
            d[cards[R]] = 1 + d.get(cards[R],0)
            sum_w += 1

           
            while sum_w > len(d) and l < R:
                if min_ == 0:
                    min_  =  sum_w
                else:
                    min_ = min(min_,sum_w)
                d[cards[l]]-=1
                if d[cards[l]] == 0:
                    del d[cards[l]]
                sum_w-=1
                l+=1
        return min_ if min_ != 0 else -1

