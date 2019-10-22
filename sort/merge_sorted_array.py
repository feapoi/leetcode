## 不利用额外的空间，把两个排序好的数组排序
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1
        i = m - 1
        j = n - 1
        while k >= 0:
            if i >= 0 and (j < 0 or nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i -= 1
            else:
                assert(j >= 0)
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        return nums1

s = Solution()
print(s.merge([1,2,3,0,0,0], 3, [2,5,6], 3))