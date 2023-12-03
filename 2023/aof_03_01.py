bath_file = "input_test_01.txt"

with open(bath_file, "r") as file:
    scheme = file.read().splitlines()
#print(scheme)

positions_set = set()

#for row in scheme:
#    print(row)

for row_index, row in enumerate(scheme):
    print(row_index, row)
    for col_index, character in enumerate(row):
        #print(col_index, character)
        if character.isdigit() or character == ".":
            continue
        #print(row_index, col_index) #1/3, 3/6, 4/3, 5/5, 8/3, 8/5

        
        for neighbor_row in range(row_index - 1, row_index + 2):
            for neighbor_col in range(col_index - 1, col_index + 2):
            #print(neighbor_col)
            
                if neighbor_row < 0:
                    continue
                elif neighbor_row >= len(scheme):
                    continue

                if neighbor_col < 0:
                    continue
                elif neighbor_col >= len(scheme[neighbor_row]):
                    continue

                current_char = scheme[neighbor_row][neighbor_col]
                if not current_char.isdigit():
                    continue
                #print(f"Position with number: {neighbor_row}, {neighbor_col}")

                while neighbor_col > 0 and scheme[neighbor_row][neighbor_col - 1].isdigit():
                    neighbor_col -= 1
                
                #print(f"Start position number: {neighbor_row}, {neighbor_col}")
                
                positions_set.add((neighbor_row, neighbor_col))
                #print(positions_set)


numbers_list = []

for row, col in positions_set:
    number_str = ""
    while col < len(scheme[row]) and scheme[row][col].isdigit():
        number_str += scheme[row][col]
        col += 1
    #print(number_str)
    numbers_list.append(int(number_str))
print(numbers_list)

result_sum = sum(numbers_list)
print(result_sum)