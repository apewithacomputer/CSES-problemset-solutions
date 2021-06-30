y = int(input())
x = list(input().split(" "))
s = 0
for i in range(0, len(x)):
    x[i] = int(x[i])
for i in range(len(x)-1):
    if x[i+1] < x[i]:
        s = s + x[i+1]-x[i]
        x[i+1] = x[i]
    elif x[i+1] > x[i]:
        pass
print(s+s*-2)
