A = 80
GLOB_MAX = [0, 0, 0]
GLOB_ITE = [0, 0, 0]
while A > 0:
    a = A
    i = 0
    max_num = 0
    while a != 1:
        if((a % 2) == 0):
            a /= 2
            a = int(a)
        else:
            a *= 3
            a += 1
            a = int(a)
        if(max_num < a) : max_num = a
        i += 1
        print(a)

    A -= 1
    print("A =", A, "en", i, "fois", "et le max_num est", max_num)

    if(GLOB_MAX[2] < max_num):
        GLOB_MAX = [A, i, max_num]
    if(GLOB_ITE[1] < i):
        GLOB_ITE = [A, i, max_num]
    
print(GLOB_ITE, GLOB_MAX)

