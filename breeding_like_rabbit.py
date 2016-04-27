series = {0:1, 1:1, 2:2}

def f(n):
    if n in series:
        return series[n]
    x = n >> 1
    if n % 2 == 0:
        series[n] = f(x) + f(x + 1) + x
    else:
        series[n] = f(x) + f(x - 1) + 1

    return series[n]

