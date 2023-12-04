class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        final_ans = 0

        tracker = ''
        k = 0
        for i in num2[::-1]:
            temp_ans = ''
            for j in num1[::-1]:
                if(tracker):
                    temp =  ( int(i) * int(j) )  + int(tracker[0])
                    tracker = ''
                    if(len(str(temp)) == 1):
                        temp_ans+=str(temp)
                    else:
                        tracker += str(temp)[0]
                        temp_ans+=str(temp)[1]
                else:
                    temp = int(i) * int(j)
                    if(len(str(temp)) == 1):
                        temp_ans+=str(temp)
                    else:
                        tracker += str(temp)[0]
                        temp_ans+=str(temp)[1]
            if(tracker):
                final_ans += int( tracker + temp_ans[::-1] + '0' * k )
            else:
                final_ans += int((temp_ans[::-1] + '0' * k ))
            
            tracker = ''
            k+=1

        return  str(final_ans)