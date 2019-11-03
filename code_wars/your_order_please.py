def order(sentence):
    if sentence == '':
        return sentence
    else:
        l = sentence.split()
        l.sort(key=find_number)
    return ' '.join(l)


def find_number(string: str):
    for s in string:
        for i in range(1, 10):
            if s == str(i):
                return i
