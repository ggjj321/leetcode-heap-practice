import heapq
class Solution(object):
    def findpower(self,num,powerdic):
        power = 0
        value = num
        
        while value != 1:
            if value in powerdic:                
                power += powerdic[value]
                break
            else:                
                power += 1
                if value % 2 == 0:
                    value /= 2                    
                else:
                    value = value * 3 + 1
        
        return power
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        powerdic = {}
        heap = []
        
        for num in range(lo,lo+k):
            powerdic[num] = self.findpower(num,powerdic)
            heapq.heappush(heap, (powerdic[num],num))
            
        for num in range(lo+k,hi+1):
            powerdic[num] = self.findpower(num,powerdic) 
            heapq.heappush(heap, (powerdic[num],num))
        
        for _ in range(k-1):
            heapq.heappop(heap)
            
        return heapq.heappop(heap)[1]
#64.71%  62.35% heap sort