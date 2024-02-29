class Solution:
    def balancedString(self, s: str) -> int:
        cur = {'Q':0,'E':0,'W':0,'R':0}
        target_num = len(s) // 4
        original = {'Q':target_num,'E':target_num,'W':target_num,'R':target_num}


        for i in s:
            cur[i]+=1
        target =  {'Q':0,'E':0,'W':0,'R':0}
        window =  {'Q':0,'E':0,'W':0,'R':0}

        for i in 'QEWR':
            if cur[i] > original[i]:
                target[i] = cur[i] - original[i]
        min_len = inf

        if sum(target.values()) == 0:
            return 0
        left = 0
        for right in range(len(s)):
            while left < right and target['Q'] <= window['Q'] and target['E'] <= window['E'] and target['R'] <= window['R'] and target['W'] <= window['W']:
                    min_len = min(min_len,sum(window.values()))
                    window[s[left]]-=1
                    left+=1
            window[s[right]] += 1
        while left < len(s) and target['Q'] <= window['Q'] and target['E'] <= window['E'] and target['R'] <= window['R'] and target['W'] <= window['W']:
                min_len = min(min_len,sum(window.values()))
                window[s[left]]-=1
                left+=1
        return min_len