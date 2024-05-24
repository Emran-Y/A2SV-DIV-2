# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] != 1:
            return False
        if len(stones) == 2:
            return stones[0] == 0 and stones[1] == 1
        
        memo = {}
        
        def can_frog_jump(current_position, jump_distance):
            if current_position == stones[-1]:
                return True
            if (current_position, jump_distance) in memo:
                return memo[(current_position, jump_distance)]
            
            for next_jump in [jump_distance - 1, jump_distance, jump_distance + 1]:
                if next_jump > 0 and current_position + next_jump in stone_positions:
                    if can_frog_jump(current_position + next_jump, next_jump):
                        memo[(current_position, jump_distance)] = True
                        return True
            
            memo[(current_position, jump_distance)] = False
            return False
        
        stone_positions = set(stones)
        return can_frog_jump(stones[1], 1)
