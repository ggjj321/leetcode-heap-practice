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


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = [(nums1[0]+ nums2[0], [nums1[0], nums2[0]],[0, 0])]
        ans = []
        finded = [ [0, 0] ]
        n1I = n2I = 0
        n1len = len(nums1)
        n2len = len(nums2)
        k = min(k,n1len * n2len)
        
        for i in range(k):
            
            minVector = heapq.heappop(heap)
            n1I = minVector[2][0]
            n2I = minVector[2][1]
            
            if ((n1I + 1) < n1len) and (n2I < n2len) and ([n1I + 1, n2I] not in finded):
                finded.append([n1I + 1, n2I])
                heapq.heappush(heap, (nums1[n1I + 1] + nums2[n2I], [nums1[n1I + 1], nums2[n2I]],[n1I + 1 ,n2I]))
                
            if (n1I < n1len) and ((n2I + 1) < n2len) and ([n1I, n2I + 1] not in finded):
                finded.append([n1I, n2I + 1])
                heapq.heappush(heap, (nums1[n1I] + nums2[n2I + 1], [nums1[n1I], nums2[n2I + 1]],[n1I ,n2I + 1]))
            
            #print(heap)
            ans.append(minVector[1])
        return ans
#optimize by 2 points .Because python dosen't have point,it replaced by index
#45.43% 70.21%