class Solution:
    def topKFrequent(self, nums, k):
        count = {}  #simple solution later i optimized 

        for n in nums:
            count[n] = count.get(n, 0) + 1

        sorted_count = sorted(count, key=count.get, reverse=True)

        return sorted_count[:k]