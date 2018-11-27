from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        hash_map = defaultdict(list)
        for s in strs:
            hash_map[''.join(sorted(s))].append(s)
        return hash_map.items()
        # return [value for _, value in hash_map.items()]

s =Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

