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
def insertion_sort(array):
    for i in range(len(array)):
        buff = array[i]
        j = i
        while (array[j - 1] > buff) and (j > 0):
            array[j] = array[j - 1]
            j = j - 1
        array[j] = buff
        text_output.append("Swap elements at indices " + str(i + 1) + " and " + str(j + 1) + ".\n")
    return array


# algorithm implementation
data = insertion_sort(data)
text_output.append("No more swaps needed.\n")


# preparation data to output
def list_to_str(list, spliterator):
    return spliterator.join(str(i) for i in list)


end_line = list_to_str(data, ' ')


# writing result to file
output_file = open('output.txt', 'w')
for line in text_output:
    output_file.write(line)
output_file.write(end_line)
output_file.close()