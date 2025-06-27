def applesAndOranges(apples,oranges,a,s,b,t):
    count_apples = 0 
    count_oranges = 0
    for i in apples:
        if i+a>=s and i+a<=t:
            count_apples += 1
    for i in oranges:
        if i+b>=s and i+b<=t:
            count_oranges += 1
    
    print(count_apples)
    print(count_oranges)