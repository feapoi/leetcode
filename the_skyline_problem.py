from heapq import *
class Solution(object):
    def getSkyline(self, buildings):
        heap=[]
        for i,(l,r,h) in enumerate(buildings):
            heap.extend([[l,"e",-h,i],[r,"l",h,i]])
        heapify(heap)
        cur=0  # current height
        height=[[0,float("inf")]]  #  a heap record [height,leaving spot] of current buildings
        ans=[]
        while heap:
            x,sgn,h,idx=heappop(heap)
            h=abs(h)
            if sgn=="e":
                heappush(height,[-h,buildings[idx][1]])    ##堆排，放入一个数
                if h>cur:
                    ans.append([x,h])
                    cur=h
            else:
                if cur==h:  # only pop the already left buildings when necessary
                    while height[0][1]<=x:
                        heappop(height)
                    cur=-height[0][0]
                    if cur<h:
                        ans.append([x,cur])
        return ans