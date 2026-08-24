import json
player_data={
    "name": "Mario",
    "level": 4,
    "items": ["mushroom", "star"],
    "is_active": True
}
with open("JSON/save_game.json","w") as file:
    json.dump(player_data, file, indent=4)

print("file printed succesfully")    