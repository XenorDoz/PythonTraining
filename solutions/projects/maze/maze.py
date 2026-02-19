import keyboard     # Might want to type `pip install keyboard` if this gives you an error
import ast          

maze = []                       # Will contain asked maze
victory = False                 # Victory checker
key_pressed = False             # Check so key is not spammed


end_position : tuple[int, int]  # End position to check for the victory
player_position: tuple[int, int]

# Custom characters, replace with any character you want here:
wall_char = "."
empty_char = " "
player_char = "O"
end_char = "X"

# We load the file into variable 
# We use replace so we can start the code from anywhere in the project
path = __file__.replace("maze.py", "mazes.txt")

def load_mazes():
    global maze

    # We open an read the file to save it as a string
    with open(path, "r") as f:
        mazes = f.read()
    
    # This lines read the string as if it was python stuff
    # So everything between [] will be transfored into arrays
    mazes = ast.literal_eval(mazes)

    # Put here what maze user wants
    choice = int(input(f"Which maze do you want ? Type from 0 to {len(mazes) - 1}: "))
    maze = mazes[choice]

def convert_symbols():
    global maze

    for y, line in enumerate(maze):
        for x, case in enumerate(line):
            match case:         # We change what value is in the maze for customization
                case 0: maze[y][x] = empty_char
                case 1: maze[y][x] = wall_char
                case 2: maze[y][x] = player_char
                case 3: maze[y][x] = end_char

def print_maze():
    for line in maze:       # Print every line
        line_string = ""     
        for case in line:   # We add every character in the line_string to print in one line
            line_string += case + " "
        print(f"{line_string}")

def get_key():
    global key_pressed

    while True:     # This is not an infinite loop because return
        event = keyboard.read_event(suppress=True)

        if event.event_type == keyboard.KEY_DOWN and not key_pressed:   # If we just pressed a key
            key_pressed = True
            return event.name

        if event.event_type == keyboard.KEY_UP:     # When we release the key
            key_pressed = False

def convert_key_to_direction(key):
    match key:
        case "w":
            return (-1, 0)
        case "a":
            return (0, -1)
        case "s":
            return (1, 0)
        case "d":
            return (0, 1)

def find_player():
    for y, line in enumerate(maze):
        for x, case in enumerate(line):
            if case == player_char:
                return (y, x)
    return (-1, -1)

def can_move(move):
    next_position = (player_position[0] + move[0],
                     player_position[1] + move[1])
    
    # If outside of top or left side of the array
    if next_position[0] < 0 or next_position[1] < 0:
        return False
    # If outside of right or bottom side of the array
    if next_position[0] >= len(maze) and next_position[1] >= len(maze[1]):
        return False 

    # If the next position is a wall
    if maze[next_position[0]][next_position[1]] == wall_char:
        return False
    
    return True

def move_player(move):
    global maze, player_position
    maze[player_position[0]][player_position[1]] = empty_char   # We empty the player position in the array
    new_position = (player_position[0] + move[0], player_position[1] + move[1])
    maze[new_position[0]][new_position[1]] = player_char                        # We add back the player in the array
    player_position = new_position                                      # We save its new position

def find_end():
    for y, line in enumerate(maze):
        for x, case in enumerate(line):
            if case == end_char:
                return (y, x)
    return (-1, -1)

def is_end():
    return player_position == end_position
        

if __name__ == "__main__":
    # Loading the maze
    load_mazes()

    # Converting the maze with custom symbols
    convert_symbols()

    # Find the positions needed
    player_position = find_player()
    end_position = find_end()
    # Game loop
    while not victory:
        print_maze()
        key = get_key()
        direction = convert_key_to_direction(key)
        if can_move(direction):
            move_player(direction)
        if is_end():
            victory = True
    print("Congrats!")
