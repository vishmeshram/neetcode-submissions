class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = dict()
        for i in nums:
            if i in arr:
                arr[i] = arr.get(i,0) + 1
            else:
                arr[i] = 1
        
        sortedkey = sorted(arr , key = arr.get , reverse = True)
        return sortedkey[:k]