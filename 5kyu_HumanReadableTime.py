# def make_readable(seconds):
#     # Do something
#     out = []
#     if 0 <= seconds <= 359999:
#         time1 = divmod(seconds,60)
#         time2 = divmod(time1[0],60)

#         hour = out.append(str(time2[0]) if time2[0]>=10 else "0{}".format(time2[0])) 
#         min = out.append(str(time2[1]) if time2[1]>=10 else "0{}".format(time2[1])) 
#         sec = out.append(str(time1[1]) if time1[1]>=10 else "0{}".format(time1[1])) 

#         return ":".join(out)

# Solution 1
def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

print(make_readable(359999))