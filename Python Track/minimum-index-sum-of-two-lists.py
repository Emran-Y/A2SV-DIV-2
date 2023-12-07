class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
      arr = []

      for i in list1:
        if(i  in list2):
          temp = list1.index(i) + list2.index(i)
          if(len(arr) == 0):
            arr.append(i)
          elif(temp < list1.index(arr[-1]) + list2.index(arr[-1])):
            arr.pop()
            arr.append(i)
          elif(temp == list1.index(arr[-1]) + list2.index(arr[-1])):
            arr.append(i)
      return arr