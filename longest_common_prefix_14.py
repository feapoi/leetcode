class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs_min_len = strs[0]
        for str in strs:
            if len(str) < strs_min_len:
                strs_min_len = str
        strs.remove(strs_min_len)
        