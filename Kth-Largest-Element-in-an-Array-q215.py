import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        kheap=nums[:k]
        heapq.heapify(kheap)
        for i in range(k,len(nums)):
            if nums[i]>=kheap[0]:
                heapq.heappop(kheap)
                heapq.heappush(kheap, nums[i])
        return kheap[0]
#81.89%  49.94%