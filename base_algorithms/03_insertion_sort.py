# reading file
input_file = open('input.txt', 'r')
lines = input_file.read().split('\n')
input_file.close()


# preparation data: parsing numbers
lines_length = int(lines[0])
data = lines[1].split(' ')
for i in range(len(data)):
    data[i] = int(data[i])
indexes = []


# realise algorithm
def insertion_sort(array):
    for i in range(len(array)):
        buff = array[i]
        j = i
        while (array[j - 1] > buff) and (j > 0):
            array[j] = array[j - 1]
            j = j - 1
        array[j] = buff
        # output new index
        indexes.append(j + 1)
    return array


# algorithm implementation
data = insertion_sort(data)


# preparation data to output
def list_to_str(list, spliterator):
    return spliterator.join(str(i) for i in list)


first_line = list_to_str(indexes, ' ')
second_line = list_to_str(data, ' ')
lines = [first_line, second_line]


# writing result to file
output_file = open('output.txt', 'w')
for line in lines:
    output_file.write(line + '\n')
output_file.close()