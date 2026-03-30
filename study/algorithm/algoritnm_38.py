# 19598번 최소 회의실 갯수
# 첫번째 줄에 배열의 크기 N이 주어진다. 둘째 줄부터N+1 줄까지 공백을 사이에 두고 회의의 시작시간과 끝나느 ㄴ시간이 주어진다.
# 시작 시간과 끝나는 시간은 2^31 = 1 보다 작거나 같은 자연수 또는 0이다.

# 출력 : 첫째 줄에 최소 회의실 개수를 출력한다.

# 그리디 알고리즘, 튜플

from queue import PriorityQueue

N = int(input())
courses = []

for _ in range(N):
    start, end = map(int, input().split())
    courses.append((start, end))

courses.sort()

pq = PriorityQueue()
pq.put(courses[0][1])
count = 1

for i in range(1, N):
    earliest = pq.get()
    if earliest <= courses[i][0]:
        pq.put(courses[i][1])
    else:
        count += 1
        pq.put(courses[i][1])
        pq.put(earliest)

print(count)