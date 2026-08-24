import json
player_data={
    "name": "Mario",
    "level": 4,
    "items": ["mushroom", "star"],
    "is_active": True
}
#dumps use korle bujhai amra print kortesi

player_string=json.dumps(player_data,indent=4)
print("This is now a stirng ----")
print(player_string)