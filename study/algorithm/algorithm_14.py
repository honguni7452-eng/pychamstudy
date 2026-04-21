# easy 14. 2217번 로프
# 그리디

N = int(input())
W = [0] * N

for i in range(N):
    W[i] = int(input())

W.sort(reverse = True)

max_weight = True
for i in range(N):
    if max_weight < W[i] * (i + 1):
        max_weight = W[i] * (i + 1)

print(max_weight)