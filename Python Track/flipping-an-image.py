class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            for j in range(len(image[i])):
                if(j > len(image[i]) - (j+1) ):
                    break
                if(j == len(image[i]) - (j+1)):
                    if(image[i][j] == 0):
                        image[i][j] = 1
                    else:
                        image[i][j] = 0
                    
                else:
                    
                    image[i][j],image[i][len(image[i]) - (j+1)] = image[i][len(image[i]) - (j+1)],image[i][j]
                    if(image[i][len(image[i]) - (j+1)] == 0):

                        image[i][len(image[i]) - (j+1)] = 1
                    else:
                        image[i][len(image[i]) - (j+1)] = 0
                    if(image[i][j] == 0):
                        image[i][j] = 1
                    else:
                        image[i][j] = 0
        return image
    
    
   