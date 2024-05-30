# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = [0]
    flag = [True]

    def merge(left_half, right_half):
        left_index = 0
        right_index = 0
        sorted_subarray = []
        sth = ''

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                sorted_subarray.append(left_half[left_index])
                left_index += 1
                if sth == '' or sth == 'left':
                    sth = 'left'
                else:
                    flag[0] = False
            else:
                if sth == '' or sth == 'right':
                    sth = 'right'
                else:
                    flag[0] = False
                sorted_subarray.append(right_half[right_index])
                right_index += 1

        sorted_subarray.extend(left_half[left_index:])
        sorted_subarray.extend(right_half[right_index:])

        return sorted_subarray

    def merge_sort(l, r, arr):
        if l == r:
            return [arr[l]]
        mid = l + (r - l) // 2

        left = merge_sort(l, mid, arr)
        right = merge_sort(mid+1, r, arr)
        if left[-1] > right[0]:
            ans[0] += 1

        return merge(left, right)
    final = merge_sort(0, len(arr) - 1, arr)
    # print(final)

    if flag[0] == False:
        print(-1)
    else:
        print(ans[0])
