n,m = map(int,input().split(' '))
nums1 = list(map(int,input().split(' ')))
nums2 = list(map(int,input().split(' ')))

p1 = 0
p2 = 0
nums = []

while(p2 < len(nums2) and p1 < len(nums1)):
    if(nums2[p2] > nums1[p1]):
        p1+=1
    else:
        nums.append(p1)
        p2+=1
while(p2 < len(nums2)):
    nums.append(p1)
    p2+=1
    
print(' '.join([str(i) for i in nums]))
