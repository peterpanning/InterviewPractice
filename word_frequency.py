def word_frequency(corprus):
    words = corprus.split(" ")
    frequencies = {}
    for word in words:
        if word in frequencies.keys():
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies