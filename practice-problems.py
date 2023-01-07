def alphabet_position(text):
    import string

    output = []
    alphabet = list(string.ascii_lowercase)

    for char in text:
        if char.isalpha():
            for i, letter in enumerate(alphabet):
                if char.lower() == letter:
                    output.append(str(i + 1))

    return " ".join(output)
