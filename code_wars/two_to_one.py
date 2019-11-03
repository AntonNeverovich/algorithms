def longest(s1, s2):
    if s1 == s2:
        return ''.join(sorted(list(s1)))
    else:
        return ''.join(sorted(set(s1) | set(s2)))


