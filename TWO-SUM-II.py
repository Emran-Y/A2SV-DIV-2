class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        storage = []
        for i in range(len(numbers)):
            if(l >= r):
                return storage
            else:
                if(numbers[l] + numbers[r] == target):
                    storage.append(1 + l)
                    storage.append(r + 1)
                    r-=1
                    l+=1
                elif(numbers[l] + numbers[r] > target):
                    r-=1
                elif(numbers[l] + numbers[r] < target):
                    l+=1
        return storage

