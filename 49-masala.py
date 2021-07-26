def yigindi_toq(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            n = n - 1
        return n + yigindi_toq(n-2)
print(yigindi_toq(5))
