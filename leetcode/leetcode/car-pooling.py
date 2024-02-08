class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * 1000

        for i in trips:
            arr[i[1]]+=i[0]
            if(i[2] < 1000):
                arr[i[2]]-=i[0]
        for i in range(1,1000):
            arr[i] = arr[i-1] + arr[i]
        for i in arr:
            if(i > capacity):
                return False
        return True


        

    