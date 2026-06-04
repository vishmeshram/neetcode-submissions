class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = defaultdict(list)
        for i in strs:
            res = tuple(sorted(i))
            
            arr[res].append(i)
        return list(arr.values())