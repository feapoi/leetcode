class Solution(object):
    def setZeroes(self, matrix):
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        ## 先对第一行 第一列赋值
        for i in range(R):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        ## 对其他行赋值
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        ## 最后处理第一行第一列当中有0的情况
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0
        if is_col:
            for i in range(R):
                matrix[i][0] = 0