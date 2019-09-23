# reading file
input_file = open('input.txt', 'r')
lines = input_file.read().split('\n')
input_file.close()


# preparation data: parsing numbers
lines_length = int(lines[0])
data = lines[1].split(' ')
indexes = range(len(data))
origin_data = []


for i in range(len(data)):
    data[i] = float(data[i])
    origin_data.append(data[i])


val = dict(zip(indexes, data))
print(val)


# realise algorithm
def insertion_sort(array):
    for i in range(len(array)):
        buff = array[i]
        j = i
        while (array[j - 1] > buff) and (j > 0):
            array[j] = array[j - 1]
            j = j - 1
        array[j] = buff
    return array


# algorithm implementation
data = insertion_sort(data)
print(val)

# calculating min, max, average values
min_val = data[0]
average_val = data[len(data) // 2]
max_val = data[len(data) - 1]


# calculating indexes of min, max, average values in origin array
def get_index(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i + 1


indexes = [get_index(origin_data, min_val), get_index(origin_data, average_val), get_index(origin_data, max_val)]


# preparation data to output
def list_to_str(list, spliterator):
    return spliterator.join(str(i) for i in list)


first_line = list_to_str(indexes, ' ')


# writing result to file
output_file = open('output.txt', 'w')
output_file.write(first_line)
output_file.close()