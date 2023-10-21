def merger():
    n , m = map(int,input().split(" "))
    nums1 = list(map(int,input().split(" ")))
    nums2 = list(map(int,input().split(" ")))
    p1 = 0
    p2 = 0
    while(p1 < n or p2 < m):
        if(p1 < n and p2 < m):
            if(nums1[p1] < nums2[p2]):
                print(str(nums1[p1]),end=' ')
                p1+=1
            else:
                print(str(nums2[p2]),end=' ')
                p2+=1
        else:
            if(p1 < n):
                print(str(nums1[p1]),end=' ')
                p1+=1
            else:
                print(str(nums2[p2]),end=' ')
                p2+=1 
    
merger()
