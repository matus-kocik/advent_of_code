def read_file(input_data):
    with open(input_data) as f:
        file = f.readline()  # readline() - str, readlines() - list[str] s n\
    return file


# Part 1:

data = "input_test.txt"
new_data = read_file(data)
print(new_data)
