def sum(l):
    s = 0
    for i in l:
        s += i
    return s
x = [68,53,70,84,60,72,51,83,70,64]
y = [288,293,349,343,290,354,283,324,340,286]
xx = [x[i] * x[i] for i in range(10)]
yy = [y[i] * y[i] for i in range(10)]
xy = [x[i] * y[i] for i in range(10)]
print(sum(yy) - sum(y) * sum(y) / 10)