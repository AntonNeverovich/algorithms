# reading file
input_file = open('input.txt', 'r')
data = input_file.read().split(" ")
input_file.close()


# calculating expression
result = int(data[0]) + int(data[1]) ** 2


# writing result to file
output_file = open('output.txt', 'w')
output_file.write(str(result))
output_file.close()