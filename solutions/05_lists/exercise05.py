# Start with that dictionary

player = {
    "name": "Alex",
    "level": 3, 
    "hp": 20}

print(player)

# Change the `"level"` value to `4`

player["level"] = 4

# Add a new key `"weapon"` with the value `"sword"`

player["weapon"] = "sword"
print(player)

# Remove the key `"hp"` using `pop()` and store it in a variable named `removed_hp`

removed_hp = player.pop("hp")

print(removed_hp)
print(player)

# Check if the key `"armor"` exists in the dictionary and display the result
# You should not make the script bug with an error!

print("armor" in player)
print(player)