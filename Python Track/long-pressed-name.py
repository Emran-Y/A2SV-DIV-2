class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        

        name_d = {}

        n = 0

        for i in range(len(name)):
            if(len(name_d) == 0):
                name_d[n] = [0,name[i]]
                name_d[n][0]+=1
            else:
                if(name[i] == name_d[n][1]):
                    name_d[n][0]+=1
                else:
                    n+=1
                    name_d[n] = [0,name[i]]
                    name_d[n][0]+=1
        typed_d= {}

        t = 0

        for j in range(len(typed)):
            if(len(typed_d) == 0):
                typed_d[t] = [0,typed[j]]
                typed_d[t][0]+=1
            else:
                if(typed[j] == typed_d[t][1]):
                    typed_d[t][0]+=1
                else:
                    t+=1
                    typed_d[t] = [0,typed[j]]
                    typed_d[t][0]+=1

        if(len(name_d) != len(typed_d)):
            return False
        for i in range(len(name_d)):
            if(typed_d[i][1] != name_d[i][1] ):
                return False
            elif(typed_d[i][0] < name_d[i][0]):
                return False

        return True
        

                
            

