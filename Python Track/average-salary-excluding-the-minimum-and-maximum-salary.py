class Solution:
    def average(self, salary: List[int]) -> float:
        x = 0
        for i in salary:
            if(i == min(salary) or i == max(salary)):
                continue
            else:
                x+=i
        return x / (len(salary) - 2)