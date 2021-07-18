import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 5:
            return n
        uglyheap = [2,3,5]
        size = 3
        i = 0
        
        maxn = 3 * n
        
        for _ in range(n - 2):
            minugly = heapq.heappop(uglyheap) 
            twoi = minugly * 2
            thri = minugly * 3
            fivi = minugly * 5
            if twoi not in uglyheap:
                heapq.heappush(uglyheap, twoi)                
            if thri not in uglyheap:
                heapq.heappush(uglyheap, thri)
            if fivi not in uglyheap:
                heapq.heappush(uglyheap, fivi)   
                
        #print(uglyheap)
                    
        return heapq.heappop(uglyheap)

#13.02% 90.23% I want to focus on heap,but it doesn't the best idea for this question.