first_list = []
second_list = []


def read_file(input_data):
    with open(input_data) as f:
        return f.read().strip()


file_data = "./input_2.txt"
data = read_file(file_data)
# print(data)
new_data = data.splitlines()

# print(new_data)

for line in new_data:
    split_line = line.split()
    first, second = map(int, split_line)
    # print(split_line)
    # print(first)
    # print(second)
    first_list.append(first)
    second_list.append(second)

#print(first_list)
#print(second_list)

score = 0

for number in first_list:
    count_in_second = second_list.count(number)
    score += number * count_in_second

print(score)