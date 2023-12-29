class Solution:
    def smallestNumber(self, num: int) -> int:

        
        

        if num > 0:


            arr = []

            for i in str(num):
                arr.append(i)
            arr.sort()
            print(arr)

            if '0' in arr:
                for i in range(len(arr)):
                    if  arr[i] != '0':
                        arr[0],arr[i] = arr[i],arr[0]
                        break
            return int(''.join(arr))


        elif num == 0:
            return 0
        else:
            arr = []
            for i in str(num)[1:]:
                arr.append(i)
            arr.sort(reverse=True)
            return  -1 * int(''.join(arr))
            

