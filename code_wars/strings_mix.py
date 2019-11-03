def mix(s1, s2):
    l1 = letter_count_to_string(s1)
    l2 = letter_count_to_string(s2)
    r = []
    min = l1 if len(l1) < len(l2) else l2
    max = l1 if len(l1) > len(l2) else l2
    for s1 in max:
        for s2 in min:
            if s1[0] == s2[0]:
                if len(s1) > len(s2):
                    r.append(str(1) + ':' + s1)
                elif len(s1) < len(s2):
                    r.append(str(2) + ':' + s2)
                else:
                    r.append('=:' + s1)

    return min, max, '/'.join(set(sorted(r)))


def how_many_letters(letter: str, string: str):
    count = 0
    for s in string:
        if letter == s:
            count += 1
    return count


def letter_count_to_string(string: str):
    l = [s for s in string if s != ' ' and s.islower()]
    s = sorted(set(map(lambda s: s * how_many_letters(s, string), l)))
    return [l for l in s if len(l) > 1]


print(mix("Are they here", "yes, they are here"))
# dd = mix("Are they here", "yes, they are here")
# print(merge_dict(dd[0], dd[1]))

