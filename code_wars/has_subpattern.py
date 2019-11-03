from tests import test as Test


def has_subpattern(string: str):
    l = len(string)
    j = 2
    count = 0
    if l == 1:
        return False
    elif l == 2:
        if string[:1] == string[1:]:
            return True
    elif l % 2 == 0:
        while j < l:
            for i in range(j - 1):
                if string[(i * l) // j: ((i + 1) * l) // j] == string[((i + 1) * l) // j: ((i + 2) * l) // j]:
                    count += 1
            j += 1
        return count > 1
    else:
        return False


Test.assert_equals(has_subpattern("a"), False)
Test.assert_equals(has_subpattern("aaaa"), True)
Test.assert_equals(has_subpattern("abcd"), False)
Test.assert_equals(has_subpattern("abababab"), True)

Test.assert_equals(has_subpattern("ababababa"), False)

Test.assert_equals(has_subpattern("123a123a123a"), True)
Test.assert_equals(has_subpattern("123A123a123a"), False)
Test.assert_equals(has_subpattern("abbaabbaabba"), True)

Test.assert_equals(has_subpattern("abbabbabba"), False)

Test.assert_equals(has_subpattern("abcdabcabcd"), False)
