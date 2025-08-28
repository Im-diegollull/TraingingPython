def sum_pares(x,y):
    sum = 0
    for i in range(x,y+1):
        if i % 2 == 0:
            sum += i
    return sum

print(sum_pares(1,10))