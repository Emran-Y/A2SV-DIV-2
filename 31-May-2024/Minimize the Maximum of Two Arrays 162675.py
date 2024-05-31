# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l = 1
        r = 1e10
        ans = -1
        lcm = math.lcm(divisor1, divisor2)

        while l <= r:
            mid = (l + r) // 2
            cnt1 = mid - mid // divisor1
            cnt2 = mid - mid // divisor2
            combined = mid - mid // lcm
            if cnt1 >= uniqueCnt1 and cnt2 >= uniqueCnt2 and combined >= uniqueCnt1 + uniqueCnt2:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return int(ans)
