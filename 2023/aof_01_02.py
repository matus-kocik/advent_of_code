import re


file_path = "2023/input_01_02.txt"
allowed_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def string_allowed_words(numbers):
    if numbers.isdigit():
        return str(numbers)
    elif numbers in allowed_words:
        return str(allowed_words.index(numbers) + 1)
    else:
        return numbers


def sum_calibration_value():
    with open(file_path, 'r') as file:
        list_of_numbers = []
        for line in file:
            numbers = [*map(string_allowed_words, re.findall("(?=(" + "|".join(allowed_words) + "|\\d))", line))]
            list_of_numbers.append(int(numbers[0] + numbers[-1]))
            
    result_sum = sum(list_of_numbers)
    print(result_sum)


sum_calibration_value()


