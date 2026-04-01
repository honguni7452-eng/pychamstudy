# 백준 13164번 행복 유치원
# 그리디 정렬

n, k = map(int, input().split())
heights = list(map(int, input().split()))

diff = []
for i in range(n - 1):
    diff.append(heights[i + 1] - heights[i])

diff.sort()

print(sum(diff[:n - k]))