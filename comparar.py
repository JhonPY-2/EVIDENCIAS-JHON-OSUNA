for i in range(len(a)):
        if a[i] > b[i]:
            a[i] = 1
            b[i] = 0
        elif a[i] < b[i]:
            a[i] = 0
            b[i] = 1
        else:
            a[i] = 0
            b[i] = 0
    return sum(a), sum(b)