r = 1000000

check = [True for _ in range(r)]

for i in range(2, int(r**0.5)):
    if check[i] ==  True:
        for j in range(i*2, r, i):
            if check[j] == True:
                check[j] = False

import sys
input = sys.stdin.readline

while True:
    n = int(input())

    if n == 0:
        break
    for i in range(3, r):
        if check[i] == True:
            if check[n-i] == True:
                print("%d = %d + %d" % (n, i, n - i))
                break
