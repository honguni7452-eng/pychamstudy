# Valid Anagram
# 문자 정렬 및 비교

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)