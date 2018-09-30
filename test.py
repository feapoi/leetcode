def fun1(n):
    res = []
    start = []
    def fun2(c = start, a = 0, b = 0):
        print(a,b,c)
        if a + b == 6:
            res.append(c)
            return
        if a < 3:
            fun2(c + '1', a + 1, b)
        if b < a:
            fun2(c + '2', a, b + 1)
    fun2()
    return res
print(fun1(1))

