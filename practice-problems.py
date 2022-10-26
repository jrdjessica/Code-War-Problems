def solution(s):
    output = []

    for i in range(0, len(s), 2):
        if i == len(s) - 1:
            output.append(s[i] + '_')
        else:
            output.append(s[i] + s[i+1])

    return output
