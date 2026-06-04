class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        arr = dict()
        for i in range(l):
            res = target - nums[i]
            if res in arr:
                return [arr[res],i]
            arr[nums[i]]=i


        