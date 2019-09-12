input_file = open('input.txt', 'r')
data = input_file.read().split(" ")
input_file.close()
result = 0


for i in range(len(data)):
    result += int(data[i])


output_file = open('output.txt', 'w')
output_file.write(str(result))
output_file.close()
