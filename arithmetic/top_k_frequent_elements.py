# problem：
#  找出数组中数量前k多的数组

#  例：   nums = [1,1,1,2,2,3], k = 2
#  结果： [1,2]
#
# solution
# 1.heapq.nsmallest
# 2.直接sort

import collections
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        return heapq.nsmallest(k, count.keys(), key = count.get)

    def topKFrequent1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        nums1 = sorted(count.items(), key=lambda x:x[1],reverse = True)[:k]
        nums2 = []
        for i in nums1:
            nums2.append(i[0])
        return nums2