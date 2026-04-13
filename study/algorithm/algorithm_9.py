# 2805 나무자르기
# 이분 탐색, 파라메트릭 서치

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
answer = 0

while left <= right:
    mid = (left + right) // 2

    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid

    if total >= M:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)