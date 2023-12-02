file_path = "input_02_01.txt"
input_cubes = {"red": 12, "green": 13, "blue": 14}

list_of_game_dicts = []
valid_game = []

with open(file_path, "r") as file:
    for line in file:
        line = line.strip().split(": ")[1].split("; ")
        game_dicts = []
        for part in line:
            part = part.split(", ")
            part_dict = {color.split()[1]: int(color.split()[0]) for color in part}
            game_dicts.append(part_dict)
        list_of_game_dicts.append(game_dicts)

for index, game in enumerate(list_of_game_dicts, start=1):
    is_valid_game = True
    for part_dict in game:
        for color in input_cubes:
            if part_dict.get(color, 0) > input_cubes[color]:
                is_valid_game = False
                break

    if is_valid_game:
        print(f"Game {index} is valid.")
        valid_game.append(index)

#print(list_of_game_dicts)
print(valid_game)
result_sum = sum(valid_game)
print(result_sum)