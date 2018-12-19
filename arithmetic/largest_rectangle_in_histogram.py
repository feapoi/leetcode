# problem：
# 求给定长条中最大的矩形
#
# solution
# 从左往右看
# 栈中只能保存递增的序列，如果碰到小的条，则把栈中序列依次出栈，计算面积
# 例如：1 2 3 4 1
# 在碰到1时，出栈 4,3,2,1
# 同时计算 4-3,4-2,4-1 的面积
# 因为是递增的序列，所以 4-3 是肯定 大于 3-2 的
#
# 例如：1,2,7,8,3,4
# 中间的 7,8 会被跳过
def max_area_histogram(histogram):
    stack = list()
    max_area = 0
    index = 0
    while index < len(histogram):
        # 如果下个条更高，则把它推到顶栈
        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1
            print(index, stack, max_area)
        # 如果下个条低，出栈一个条，并计算面积
        else:
            top_of_stack = stack.pop()
            # 这里注意stack[-1] + 1 和 top_of_stack不一定是相等的，中间可能去除了几个大数
            area = (histogram[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))
            max_area = max(max_area, area)
            print(index, stack, max_area, top_of_stack)
    # 把剩余的条都出栈，计算面积
    while stack:
        top_of_stack = stack.pop()
        area = (histogram[top_of_stack] *
                ((index - stack[-1] - 1)
                 if stack else index))
        max_area = max(max_area, area)
        print(index, stack, max_area, top_of_stack)
    return max_area

hist = [1,1,6,7,2,2,2,3,3,3,4,4,4,4]
print("Maximum area is",
      max_area_histogram(hist))
