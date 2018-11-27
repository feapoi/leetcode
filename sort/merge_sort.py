def merge_sort(List):
    this_len = len(List)
    mid = this_len // 2
    if this_len > 1:
        left_list = merge_sort(List[:mid])
        right_list = merge_sort(List[mid:])
    else:
        left_list = []
        right_list = List
    result_list = []
    while left_list != [] and right_list != []:
        if left_list[0] > right_list[0]:
            result_list.append(right_list[0])
            right_list = right_list[1:]
            print(right_list)
        else:
            result_list.append(left_list[0])
            left_list = left_list[1:]
            print(right_list)
    result_list = result_list + left_list + right_list
    return result_list


print(merge_sort([4,6,7,1,8,9,3,4,6]))