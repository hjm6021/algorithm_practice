def snail(snail_map):
    expected = []
    n, m = len(snail_map), len(snail_map[0]) 
    print(n, m)
    if n < 1 or m < 1:
        return expected
        
    for i in range(2*n-1):
        x, y = divmod(i, 4)
        if y == 0:
            for a in range(x, n-x):
                expected.append(snail_map[x][a])
        elif y == 1:
            for b in range(x+1, n-x):
                expected.append(snail_map[b][-x-1])
        elif y == 2:
            for c in range(n-x-2, x-1, -1):
                expected.append(snail_map[-x-1][c])
        else:
            for d in range(n-x-2, x, -1):
                expected.append(snail_map[d][x])

    return expected

# # others solution#1
# def snail(array):
#     ret = []
#     if array and array[0]:
#         size = len(array)
#         for n in xrange((size + 1) // 2):
#             for x in xrange(n, size - n):
#                 ret.append(array[n][x])
#             for y in xrange(1 + n, size - n):
#                 ret.append(array[y][-1 - n])
#             for x in xrange(2 + n, size - n + 1):
#                 ret.append(array[-1 - n][-x])
#             for y in xrange(2 + n, size - n):
#                 ret.append(array[-y][n])
#     return ret

# # others solution#2
# import numpy as np

# def snail(array):
#     m = []
#     array = np.array(array)
#     while len(array) > 0:
#         m += array[0].tolist()
#         array = np.rot90(array[1:])
#     return m

# array = [[]]
# print(snail(array))
