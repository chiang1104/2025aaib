#LeetCode 1. Two Sum
#有一堆數字 nums 裡面哪兩個相加,是 target
#nums[i] + nums[j] == target 找到i和j使得加起來是target
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        box={} #有一個箱子,裡面放出過的數字
        #我們想要湊出target這個加總

        for i, num in enumerate(nums):
            other = target-num #另外一個需要的數可以湊出target的(target-num)
            if other in box: #在箱子裡,有另一個需要的數
                return[box[other],i] #找到答案
            else: #如果沒有合適的數字能湊
                box[num] = i #就把現在的數字num,放到box裡面
