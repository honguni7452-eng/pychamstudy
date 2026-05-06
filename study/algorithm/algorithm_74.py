# easy74. 2491번 수열
# 구현, 길이 누적

N = int(input())
arr = list(map(int, input().split()))

up = 1
down = 1
answer = 1

for i in range(1, N):
    if arr[i - 1] <= arr[i]:
        up += 1
    else:
        up = 1

    if arr[i - 1] >= arr[i]:
        down += 1
    else:
        down = 1

    answer = max(answer, up, down)

print(answer)