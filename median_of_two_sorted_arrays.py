class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        flag = 0
        sum = len(nums1) + len(nums2)
        if sum % 2 == 0:
            flag = 1
        median = int((len(nums1) + len(nums2)) / 2)
        result = self.mergeArray(nums1, nums2, median)
        print(result)
        if flag == 0:
            return result[median]
        else:
            return (result[median] + result[median - 1])/2

    def mergeArray(self, nums1, nums2, median):
        result = []
        index = 0
        n1 = 0
        n2 = 0
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        while index != median + 1:
            if n1 == nums1_len:
                index += 1
                result = result + [nums2[n2]]
                n2 += 1
            elif n2 == nums2_len:
                index += 1
                result = result + [nums1[n1]]
                n1 += 1
            elif nums1[n1] < nums2[n2]:
                index += 1
                result = result + [nums1[n1]]
                n1 += 1
            else:
                index += 1
                result = result + [nums2[n2]]
                n2 += 1
        return result

s = Solution()
print(s.findMedianSortedArrays([1,3,5], [2,4]))