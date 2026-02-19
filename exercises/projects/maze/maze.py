# Importing libraries
import keyboard     # Might want to type `pip install keyboard` if this gives you an error
import ast          

# Custom characters, replace with any character you want here:

wall_char = ""
empty_char = ""
player_char = ""
end_char = ""

# We load the file into variable 
# We use replace so we can start the code from anywhere in the project
path = __file__.replace("maze.py", "mazes.txt")

def load_mazes():
    """
    Loads maze from the file in 'path' variable
    Then, asks for user which maze he wants to use
    """
    global maze

    # We open an read the file to save it as a string
    with open(path, "r") as f:
        mazes = f.read()
    
    # This lines read the string as if it was python stuff
    # So everything between [] will be transfored into arrays
    mazes = ast.literal_eval(mazes)

    #######################
    # Put here your code! #
    #######################

def convert_symbols():
    """
    Takes the global maze variable
    Modify its values with customizable chars given at the top of the script
    Simply aesthetics stuff, but great looking!
    """
    pass

def print_maze():
    """
    Displays the maze in a clearer way than simply using print(maze)
    Should display every line with the customized character
    (You can add a space after every char to make it proportionally good)
    """
    pass

def get_key():
    """
    Waits for a key input and returns what key is pressed
    To know when a key is interacted:
        -> keyboard.read_event(suppress = True)
        Returns an event, 'suppress' makes so you don't actually type
    The event has different attributes like 'event_type' or 'name'
    -> 'event_type' is stuff like 'keyboard.KEY_UP' or 'keyboard.KEY_DOWN'
    -> 'name' is what key is pressed as a string
    """
    pass

def convert_key_to_direction(key):
    """
    Takes a key as parameter, type should be string but up to you if you send an event or something
    Returns a tuple indicating what direction should we be looking
    You can use 'match key', it's like using an if/else but better, go check online!
    """
    pass

def find_player():
    """
    Checks in the maze array where is located the player
    """
    pass

def can_move(move):
    """
    Takes a move as parameter, should be a tuple of (int, int)
    Checks if next position done with that move is valid or not
    """
    pass

def move_player(move):
    """
    Takes a move as parameter, should be a tuple of (int, int)
    Moves the player in the maze array
    """
    pass

def find_end():
    """
    Checks in the maze array where is located the player
    """
    pass

def is_end():
    """
    Checks if the player is on the end case
    """
    pass

if __name__ == "__main__":
    pass
