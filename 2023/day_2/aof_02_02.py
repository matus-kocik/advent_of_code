file_path = "input_02_02.txt"

list_of_game_dicts = []
result_sum = 0

with open(file_path, "r") as file:
    for line in file:
        line = line.strip().split(": ")[1].split("; ")
        game_dicts = []
        for part in line:
            part = part.split(", ")
            part_dict = {color.split()[1]: int(color.split()[0]) for color in part}
            game_dicts.append(part_dict)
        list_of_game_dicts.append(game_dicts)


for item_line in list_of_game_dicts:
    love_dict = {}
    for item in item_line:
        for key, value in item.items():
            if key not in love_dict:
                love_dict[key] = value
            else:
                love_dict[key] = max(love_dict[key], value)
    
    x = 1
    for value_dict in love_dict.values():
        x *= value_dict
    result_sum += x
    
print(result_sum)