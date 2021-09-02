import re
def mix(s1, s2):
    result = []
    s1 = re.sub(r"[^a-z]", '', s1)
    s2 = re.sub(r"[^a-z]", '', s2)
    s1 = count_alphabet(s1)
    s2 = count_alphabet(s2)
    output1 = [key for key, value in s1.items()]
    output2 = [key for key, value in s2.items()]
    output = set(output1+output2)

    for alphabet in output:
        if alphabet in s1 and not alphabet in s2:
            result.append("1:{}".format(alphabet*s1[alphabet]))
        elif not alphabet in s1 and alphabet in s2:
            result.append("2:{}".format(alphabet*s2[alphabet]))
        else:
            if s1[alphabet] > s2[alphabet]:
                result.append("1:{}".format(alphabet*s1[alphabet]))
            elif s1[alphabet] == s2[alphabet]:
                result.append("=:{}".format(alphabet*s1[alphabet]))
            else:
                result.append("2:{}".format(alphabet*s2[alphabet]))

    result = sorted(result, key=lambda x: (-len(x), x))
    return "/".join(result)

def count_alphabet(string):
    count = {}
    for i in string:
        if string.count(i) > 1:
            count[i] = string.count(i)
    return count

print(mix("Are they here", "yes, they are here"))