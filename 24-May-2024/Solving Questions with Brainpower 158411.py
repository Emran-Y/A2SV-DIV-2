# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        num_questions = len(questions)
        memo = [-1] * num_questions

        def solve_question(index):
            if index >= num_questions:
                return 0
            if memo[index] != -1:
                return memo[index]
            
            points = questions[index][0]
            brainpower = questions[index][1]
            
            take_points = points + solve_question(index + brainpower + 1)
            skip_points = solve_question(index + 1)
            
            memo[index] = max(take_points, skip_points)
            return memo[index]
        
        return solve_question(0)
