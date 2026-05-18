import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        # build freq
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for item, freq in freq.items():
            # O(n * log(K))
            if len(heap) >= k:
                heapq.heappushpop(heap, (freq, item))
            else:
                heapq.heappush(heap, (freq, item))

        # You may return the output in any order (therefore heap works)
        return [item for _, item in heap]

