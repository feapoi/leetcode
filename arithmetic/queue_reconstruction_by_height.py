# problem：
#  一个无序的数组中有多个元素，每个元素为含有两个元素的数组
#  第一个值表示大小，第二个值表示在他之前有多少个大于等于他的元素
#  按照此规则把无序的元素整理成有序
#  例：   [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#  结果： [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#
# solution
# 先进行排序，然后按规则在结果中插入数据
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]]
        """
        if not people:
            return []
        people.sort(key = lambda x:int(x[1]))
        people.sort(key = lambda x:int(x[0]),reverse = True)
        res = [people[0]]
        for i in range(1, len(people)):
            tempCount = 0
            resLen = len(res)
            for j in range(resLen):
                if res[j][0] >= people[i][0]:
                    tempCount += 1
                else:
                    res.insert(j, people[i])
                    break
                if tempCount > people[i][1]:
                    res.insert(j, people[i])
                    break
                if j + 1 == len(res):
                    res.append(people[i])
        return res

print(Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))