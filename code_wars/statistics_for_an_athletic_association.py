def stat(strg: str):
    l = [str_to_time(s.replace(',', '')) for s in strg.split()]
    if l:
        rng = time_to_str(max(l) - min(l))
        avr = time_to_str(sum(l) // len(l))
        med = time_to_str(median(l))
        return 'Range: {0} Average: {1} Median: {2}'.format(rng, avr, med)
    else:
        return ''


def median(nums: []):
    l = len(nums)
    nums.sort()
    if l % 2 != 0:
        return nums[(l // 2)]
    else:
        return (nums[(l // 2)] + nums[(l // 2) - 1]) / 2


def str_to_time(string: str):
    t = string.split('|')
    h = int(t[0])
    m = int(t[1])
    s = int(t[2])
    return h * 60 * 60 + m * 60 + s


def time_to_str(time: int):
    h = int(time // 3600)
    m = int((time % 3600) // 60)
    s = int(time - (h * 3600) - (m * 60))
    return '{0}|{1}|{2}'.format(str(h).zfill(2), str(m).zfill(2), str(s).zfill(2))

#
# print(median([3, 5, 6, 9]))
# print(median([3, 3, 5, 9, 11]))
# print(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))
# print(stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41"))
