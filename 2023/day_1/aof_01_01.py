import re

file_path = "input_01_01.txt"



def sum_calibration_value():
    with open(file_path, 'r') as file:
        list_of_numbers = []
        for line in file:
            numbers = re.findall(r'\d', line)
            list_of_numbers.append(int(numbers[0] + numbers[-1]))
            
        result_sum = sum(list_of_numbers)

    print(result_sum)
    
    
sum_calibration_value()


