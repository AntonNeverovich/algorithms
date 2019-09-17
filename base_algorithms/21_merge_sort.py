# reading file
input_file = open('input.txt', 'r')
lines = input_file.read().split('\n')
input_file.close()


# preparation data: parsing numbers
lines_length = int(lines[0])
data = lines[1].split(' ')
origin_data = []
text_output = []
for i in range(len(data)):
    data[i] = int(data[i])
    origin_data.append(data[i])


# realise algorithm
def merge(a, b):
    i, j, = 0, 0
    n, m = len(a), len(b)
    c = []
    while i < n or j < m:
        if j == m or (i < n and a[i] <= b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c


# recursive algorithm
def merge_sort(a):
    line = ''
    n = len(a)
    if n == 1:
        return a
    mid = n // 2
    x = a[:mid]
    #  index If
    line = str(1) + ' '
    y = a[mid:]
    line += str(len(y)-1) + ' '
    line += str(x[0]) + ' ' + str(y[len(y)-1]) + '\n'
    text_output.append(line)
    x = merge_sort(x)
    y = merge_sort(y)
    return merge(x, y)


# algorithm implementation
res = merge_sort(data)
print res


# preparation data to output
def list_to_str(list, spliterator):
    return spliterator.join(str(i) for i in list)


end_line = list_to_str(res, ' ')


# writing result to file
output_file = open('output.txt', 'w')
for line in text_output:
    output_file.write(line)
output_file.write(end_line)
output_file.close()