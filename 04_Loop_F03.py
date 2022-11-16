def grade_mcq(sol, ans):
    x = sol
    s = ans
    c = 0
    if len(x)!=len(s):
        return -1
    else:
        for i in range(len(x)):
            if x[i]==s[i]:
                c += 1
        return c

exec(input())