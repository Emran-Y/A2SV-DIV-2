class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        table = {5:0,10:0}

        for i in bills:
            if i == 5:
                table[5] = 1 + table.get(5,0)
            elif i == 10:
                if table[5] >= 1:
                    table[5] = table.get(5,0) - 1
                    table[10] = 1 + table.get(10,0)
                else:
                    return False
            else:
                if table[10] >= 1 and table[5] >=1:
                    table[5] = table.get(5,0) - 1
                    table[10] = table.get(10,0) - 1
                elif table[5] >= 3:
                    table[5] = table.get(5,0) - 3

                else:
                    return False
        return True
            