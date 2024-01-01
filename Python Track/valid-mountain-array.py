class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if(len(arr) < 3):
            return False

        prev = arr[0]
        up = True

        for R in range(1,len(arr)):
            if(up):
                if(arr[R] > prev):
                    prev = arr[R]
                elif(arr[R] == prev):
                    return False
                else:
                    if(R == 1):
                        return False
                    prev = arr[R]
                    up = False
            else:
                if(arr[R] < prev):
                    prev = arr[R]
                elif(arr[R] == prev):
                    return False
                else:
                    return False
        if(up):
            return False
        return True

        