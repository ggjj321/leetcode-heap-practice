import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap = []
        self.minheap = []
        self.numlist = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.numlist.append(num)
        if len(self.numlist) == 1:
            return
                
        if len(self.numlist) == 2:
            heapq.heappush(self.maxheap, min(self.numlist) * -1)
            heapq.heappush(self.minheap, max(self.numlist))
            
        
        else:
            maxlen = len(self.maxheap)
            minlen = len(self.minheap)
            
            if maxlen > minlen:
                median = self.maxheap[0] * -1  #奇數預設在maxheap            
            else:
                median = (self.maxheap[0] * -1 + self.minheap[0]) / 2.0
            
            if num > median:
                heapq.heappush(self.minheap, num)
                minlen += 1
            else:
                heapq.heappush(self.maxheap, -1 * num)
                maxlen += 1
            
            if minlen - maxlen >= 1:
                heapq.heappush(self.maxheap, -1 * heapq.heappop(self.minheap))
            if maxlen - minlen > 1:
                heapq.heappush(self.minheap, -1 * heapq.heappop(self.maxheap))
            
    def findMedian(self):
        """
        :rtype: float
        """
        #print(self.maxheap,self.minheap)
        if len(self.numlist) == 1:
            return self.numlist[0]
        if len(self.numlist) % 2 == 0:
            return (-1.0 * self.maxheap[0] + self.minheap[0]) / 2.0            
        else:
            return -1.0 * self.maxheap[0]
#26.99% 5.18% ,max heap and min heap