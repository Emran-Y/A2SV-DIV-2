class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if arr == sorted(arr):
            return []
        ans=[]       
        def reverse(arr,k):
            subArr = arr[:k]
            rest = arr[k:]
            subArr.reverse()
            arr = subArr + rest
            return arr
   

        while arr != sorted(arr) and len(arr) > 0:
            maxim = arr.index(max(arr))
            arr = reverse(arr,maxim + 1 )
            ans.append(maxim +1)
            arr = reverse(arr, len(arr))
            ans.append(len(arr))
            arr.pop()
        

        return ans