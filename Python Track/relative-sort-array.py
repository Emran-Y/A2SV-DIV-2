class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        final = []
        for i in arr2:
            for j in arr1:
                if(i == j):
                    final.append(j)
        segete = []
        for i in arr1:
            if (i not in arr2):
                segete.append(i)
        segete.sort()
        return final + segete