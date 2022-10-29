def narcissistic(value):
    power = len(str(value))

    string_val = str(value)

    output = 0

    for num in string_val:
        output += int(num) ** power

    if output == value:
        return True
    return False
