# conditions: translate text
a = ["g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr",
     "amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q",
     "ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.",
     "lmu ynnjw ml rfc spj."]

# data preparation
data = []
result = []
for i in range(len(a)):
    data += a[i].split()

# replacing algorithm
for i in range(len(data)):
    letters = list(data[i])
    for j in range(len(letters)):
        if 97 <= ord(letters[j]) <= 120:
            letters[j] = chr(ord(letters[j]) + 2)
        if ord(letters[j]) == 121:
            letters[j] = 'a'
        if ord(letters[j]) == 122:
            letters[j] = 'b'
        result.append(letters[j])
    result.append(' ')

# result output
result = ''.join(str(e) for e in result)
print result


