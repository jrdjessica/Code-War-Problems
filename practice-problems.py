def find_short(s):
    word_list = s.split(' ')

    shortest = len(word_list[0])

    for word in word_list:
        if len(word) < shortest:
            shortest = len(word)

    return shortest
