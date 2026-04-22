# easy 62. 19941번 햄버거 분배
# 그리디 알고리즘

from queue import PriorityQueue

N, K = map(int, input().split())
S = input()

pq = PriorityQueue()
for i in range(N):
    if S[i] == 'H':
        pq.put(i)

count = 0
for i in range(N):
    if S[i] == 'P':
        while pq.qsize() > 0:
            x = pq.get()

            if abs(x - 1) <= K:
                count += 1
                break

            if x < i:
                continue
            else:
                pq.put(x)
                break
print(count)
