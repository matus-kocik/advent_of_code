def read_file(input_data):
    with open(input_data) as f:
        file = f.read()  # readline() - str, readlines() - list[str] s n\
    return file


# Part 1:


""" floor = 0
for i in file:
    if i == "(":
        floor += 1
    else:
        floor -= 1
print(floor) """


data = "./input_1.txt"
floor = sum(+1 if i == "(" else -1 for i in read_file(data))
print(floor)

data = "./input_1.txt"
floor_1=read_file(data).count("(") - read_file(data).count(")")
print(floor_1)

# Part 2:

data = "./input_2.txt"
new_data = read_file(data)

i = 0
for x, y in enumerate(new_data):
    if y == ")":
        i -= 1
    else:
        i += 1
    if i == -1:
        print(x+1)
        break
