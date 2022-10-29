def spin_words(sentence):
    output = []

    words = sentence.split(' ')

    for word in words:
        if len(word) < 5:
            output.append(word)
        else:
            rev_letters = reversed(word)
            output.append(''.join(rev_letters))

    return ' '.join(output)
