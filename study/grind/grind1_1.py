# Two Sum
# 해시맵, 시간복잡도

class Solution(object):
    def twoSum(self, nums, target):
        dic = {} # 숫자, 인덱스 저장할 dic

        for i in range(len(nums)): # 배열 전체 순회
            need = target - nums[i]

            if need in dic: # 필요한 숫자가 이전에 등장했는지 확인
                return [dic[need], i] # 있다면 이전 인덱스와 현재 인덱스 반환

            dic[nums[i]] = i