
first_list = []
second_list = []

def read_file(input_data):
    with open(input_data) as f:
        return f.read().strip()


file_data = "./input_1.txt"
data = read_file(file_data)
# print(data)
new_data = data.splitlines()

# print(new_data)

for line in new_data:
    split_line = line.split()
    first, second = map(int, split_line)
    #print(split_line)
    #print(first)
    #print(second)
    first_list.append(first)
    second_list.append(second)

# print(first_list)
# print(second_list)

first_list.sort()
second_list.sort()
#print(first_list)
#print(second_list)

#complet_list = zip(first_list, second_list)
#print(list(complet_list))

distance = 0

for first_number, second_number in zip(first_list, second_list):
    difference = abs(first_number - second_number)
    distance += difference

print(distance)