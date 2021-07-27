def solution(args):
    # your code here
    start = 0
    result = ""
    
    for i, value in enumerate(args):
        if i == len(args)-1 or args[i+1] != value+1:
            if i-start < 2:
                for j in range(start, i+1):
                    result += str(args[j]) + ","
            else:
                result += str(args[start]) + "-" + str(args[i])	+ ","
            start = i+1
        else:
            continue
    
    return result[:-1] 

print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
            
            