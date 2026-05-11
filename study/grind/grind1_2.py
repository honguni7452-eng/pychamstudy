# Valid Parentheses
# 스택, 시간 복잡도

class Solution(object):
    def isValid(self, s):
        stack = []

        dic = {
            ')': '(',
            ']': '[',
            '}': '{'
        } # 닫는 괄호 기준으로 짝 저장

        for ch in s: # 문자열 전체 순회
            if ch in dic.values(): # 여는 괄호인지 확인
                stack.append(ch) # 맞다면 스택에 저장

            else:
                if not stack:
                    return False # 닫는 괄호인데 스택이 비어있으면 false

                top = stack.pop() # 가장 최근 여는 괄호 꺼내기

                if dic[ch] != top:
                    return False # 짝이 안 맞으면 false

        return len(stack) == 0 # 모든 괄호 처리 후 스택이 비어있어야 올바른 괄호

