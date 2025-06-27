def kangaroo(x1, v1, x2, v2):
 for i in range(10000):
       if x1 == x2:
        return "YES"
       x1 +=v1
       x2 += v2
 return "NO"