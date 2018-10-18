# problem：
# 给定n组括号，问有多少合法的组合方式
#  例  n = 3
#  结果 ["((()))","(()())","(())()","()(())","()()()"]
#

# Backtracking 回溯
# return 会返回到最靠近的一个分歧点
def fun1(n):
    res = []
    start = ''
    def fun2(c = start, a = 0, b = 0):
        if a + b == 2 * n:
            print("end")
            res.append(c)
            return
        if a < n:
            print(1)
            fun2(c + '(', a + 1, b)
        print("----------------")
        if b < a:
            print(2)
            fun2(c + ')', a, b + 1)
    fun2()
    return res

# Closure Number 闭包数
# g(0) = ['']   g(1) = ['()']
# 总的类型只有 [()()] 和 [(())] 这两种，其余都由这两种组合而成
# 下面的方法就是用这两种来组合
def generateParenthesis(N):
    if N == 0: return ['']
    ans = []
    for c in range(N):
        for left in generateParenthesis(c):
            for right in generateParenthesis(N-1-c):
                print('({}){}'.format(left, right))
                ans.append('({}){}'.format(left, right))
    return ans

print(fun1(3))