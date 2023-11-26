import time

début = time.time()

n = 100
for i in range(n):
    for j in range(n):
        print(i, j)

fin = time.time()

print("Temps :", round(1000*(fin - début), 0), "ms")