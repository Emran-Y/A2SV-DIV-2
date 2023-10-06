class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+=1
        sorted_dict = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
        text = ''
        for key,value in sorted_dict.items():
            text+=key * value
        return text
