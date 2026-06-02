# 409. Longest Palindrome
# 시간 복잡도

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        answer = 0
        has_odd = False

        for value in count.values():
            if value % 2 == 0:
                answer += value
            else:
                answer += value - 1
                has_odd = True

        if has_odd:
            answer += 1

        return answer