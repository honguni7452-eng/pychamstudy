# N과 M (2)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오

# 1부터 N까지 자연수 중에서 중복없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

# Combination(a, n) -> 배열 a에서 n개를 뽑는 경우를 인덱스의 사전순으로 반환


from itertools import combinations

N, M = map(int, input().split())

for combation in combinations(range(1, N+1),  M):
    print(*combation)