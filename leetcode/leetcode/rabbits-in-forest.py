class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        table = {}

        for i in answers:
            table[i] = 1 + table.get(i,0)
        min_num_of_rabbits = 0

        for key,value in table.items():
            if key == 0:
                min_num_of_rabbits+=value
                continue
            if value <= key + 1:
                min_num_of_rabbits+=key + 1
            else:
                group = math.ceil(value/(key+1))
                min_num_of_rabbits+=group * (key + 1)
        return min_num_of_rabbits


