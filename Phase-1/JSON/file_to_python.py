import json
with open("JSON/save_game.json","r") as file:
    data=json.load(file)

print(f"Welcome back player {data['name']}")    
print(f"Your lvel is {data['level']}")