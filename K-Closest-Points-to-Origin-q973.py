import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def calcu(x,y):
            return x ** 2 + y ** 2
        
        heap = []
        ans = []
        
        for point in points[:k]:
            distance = calcu(point[0], point[1])
            heapq.heappush(heap,(distance, point[0],point[1]))
        
        for point in points[k:]:
            distance = calcu(point[0], point[1])            
            heapq.heappush(heap,(distance, point[0],point[1]))
            #heap = heap[:k]
            
        #print(heap)
        for _ in range(k):
            vector = heapq.heappop(heap)
            ans.append([ vector[1], vector[2] ])
            
        return ans
#49.06% 28.60%

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def calcu(point):
            return point[0] ** 2 + point[1] ** 2
            
        return sorted(points , key = calcu)[:k]
#built in sort 98.75% 93.56%