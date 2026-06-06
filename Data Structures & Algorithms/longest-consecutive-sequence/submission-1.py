class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        lset = set(nums)

        largestnum = 0

        for num in lset:

            if (num -1) not in lset:
                current = num
                currentnum = 1

                while (current + 1) in lset:
                    current += 1
                    currentnum += 1

                largestnum = max(largestnum,currentnum)
        return largestnum



