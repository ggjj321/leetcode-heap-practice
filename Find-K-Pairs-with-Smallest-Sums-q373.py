import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap=[]
        ans=[]
        
        for n1 in nums1:
            for n2 in nums2:
                heapq.heappush(heap, (n1+n2,[n1,n2]))
        
        for _ in range(k):
            if len(heap):
                ans.append(heapq.heappop(heap)[1])
            
        return ans
#16.19% 13.58% brute force