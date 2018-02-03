x = [-1, 0, 3, 2, 1, -3, -4]
result = []
x.sort()
a=len(x)-1
for i in range(len(x)-2):
    l = i + 1
    while (l < a):
        sum_ = x[i] + x[l] + x[a]
        if (sum_ < 0):
            l = l + 1
        if (sum_ > 0):
            a = a - 1
        if not sum_:
            result.append([x[i],x[l],x[a]])
            l = l + 1
print(result)