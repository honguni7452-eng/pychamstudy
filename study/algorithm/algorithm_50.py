#  9375번 패션왕 신해빈
# 딕셔너리로 종류별 갯수 카운트

T = int(input())

for _ in range(T):
    N = int(input())

    count = {}
    for _ in range(N):
        _, t = input().split()

        if t not in count:
            count[t] = 0
        count[t] += 1

    answer = 1
    for k, v in count.items():
        answer *= (v + 1)
    answer -= 1
    print(answer)