class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = []
        table = {}

        for i in range(len(tickets)):
            table[i] = tickets[i]

        for i in range(len(tickets)):
            queue.append([tickets[i],i])
        
        count = 0


        while table[k] > 0:
            count+=1
            queue[0][0] = queue[0][0] - 1
            if queue[0][1] == k:
                table[k]-=1
            if(queue[0][0] == 0):
                queue.pop(0)
                continue
            queue.append(queue.pop(0))
        return count
            
            

