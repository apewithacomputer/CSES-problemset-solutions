x = int(input())
n = list(range(1, x+1))
t = 0
even = []
odd =[]

for i in n:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
n = even + odd  

if x == 3 or x == 2:
    print("NO SOLUTION")
else:
    print(*n)