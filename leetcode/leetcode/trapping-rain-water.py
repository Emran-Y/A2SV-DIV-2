class Solution:
    def trap(self, height: List[int]) -> int:
        stack =  []
        water = 0

        for index,value in enumerate(height):
            while stack and value > stack[-1][0]:
                val,idx = stack.pop()
                if stack and stack[-1][0] < val:
                    continue
                if stack:
                    left_border, j = stack[-1]
                    # we compute the water
                    edge = left_border if left_border < value else value
                    water += (edge - val)*(index-j-1)
            stack.append((value,index))
        return water