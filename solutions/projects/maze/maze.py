import keyboard     # Might want to type `pip install keyboard` if this gives you an error
import ast          

maze = []                       # Will contain asked maze
end_position : tuple[int, int]  # End position to check for the victory
victory = False                 # Victory checker

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
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        match event.name:
            case "w":
                print("up")
            case "a":
                print("left")
            case "s":
                print("down")
            case "d":
                print("right")


if __name__ == "__main__":
    # Loading the maze
    load_mazes()

    # Converting the maze with custom symbols
    convert_symbols()

    # Game loop
    while not victory:
        print_maze()
    pass