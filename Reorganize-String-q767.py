import heapq
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        lists = list(s)
        fdic = {}
        heap = []
        ans = []
        
        for charc in lists:
            if charc not in fdic:
                fdic[charc] = 1
            else:
                fdic[charc] += 1
        
        for charc in fdic:
            heapq.heappush(heap, (-fdic[charc], charc))
            
        while len(heap) > 1:
            current = heapq.heappop(heap)[1]
            nextchar = heapq.heappop(heap)[1]
            ans.append(current)
            ans.append(nextchar)
            fdic[current] -= 1
            fdic[nextchar] -= 1
            if fdic[current] > 0:
                heapq.heappush(heap, (-fdic[current], current))
            if fdic[nextchar] > 0:
                heapq.heappush(heap, (-fdic[nextchar], nextchar))
        
        if len(heap) > 0:
            last = heapq.heappop(heap)[1]
            if fdic[last] > 1:
                return ""
            ans.append(last)
            
        return "".join(ans)
'''
99.53% 10.69% greedy,hash map,max heap
I have had hash map,max heap and some greedy idea,but I don't know how to build the string.
the idea was referenced by
https://www.youtube.com/watch?v=zaM_GLLvysw&list=WL&index=43&t=1s
'''