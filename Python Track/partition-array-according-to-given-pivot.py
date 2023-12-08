class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr_L = []
        arr_R = []
        arr_E = []

        for i in nums:
            if(i > pivot):
                arr_R.append(i)
            elif(i < pivot):
                arr_L.append(i)
            else:
                arr_E.append(i)
        return arr_L + arr_E + arr_R