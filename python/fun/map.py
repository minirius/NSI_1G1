def map(value , start1, end1, scale1, scale2):
    #
    # value         scaleValue
    # val2 - val1   scale2 - scale1
    #
    return ((value*(scale2 - scale1))/(end1 - start1)) + scale1

print(map(5, 0, 10, 50, 150))