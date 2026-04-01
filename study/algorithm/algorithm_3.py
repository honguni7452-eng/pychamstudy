# 백준 14916번 거스름돈
# 그리디, 정렬

n = int(input())

answer = -1

for five in range(n // 5, -1, -1):
    remain = n - five * 5

    if remain % 2 == 0:
        answer = five + (remain // 2)
        break

print(answer)