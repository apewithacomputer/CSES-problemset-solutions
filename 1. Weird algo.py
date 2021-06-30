x = int(input())

print(x,end=" ")
while x != 1:
    if x%2 == 0:
        x = x/2
    elif x%2 != 0:
        x = x*3
        x = x+1
    print(int(x), end=" ")
