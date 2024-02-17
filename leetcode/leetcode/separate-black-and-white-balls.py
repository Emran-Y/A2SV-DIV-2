class Solution:
    def minimumSteps(self, s: str) -> int:
        left = 0
        right = 1
        minimum_number_of_steps = 0
        list_of_balls = list(s)
        while right < len(s):
            if list_of_balls[left] == '0' and list_of_balls[right] == '0':
                right+=1
                left+=1
            elif list_of_balls[left] == '0' and list_of_balls[right] == '1':
                right+=1
                left+=1

            elif list_of_balls[left] == '1' and list_of_balls[right] == '0':
                list_of_balls[left],list_of_balls[right] = '0','1' 
                minimum_number_of_steps+=right - left
                right+=1
                left+=1
            else:
                right+=1
        return minimum_number_of_steps