class Solution:
    def arraySortedOrNot(self, arr, n):
        l = 0
        r = 1
        for i in range(n):
            if(r>=n):
                return 1
            else:
                if(arr[r] >= arr[l]):
                    l+=1
                    r+=1
                else:
                    return 0
