maze[0] is just an empty square to test moves
next ones are mazes

A. Maze loading
- load_maze()  
  choose what maze will be used 
- convert_symbols()
  By default, you'll have from 0 to 3:
  - 0 is empty case
  - 1 is wall
  - 2 is player
  - 3 is end  
  Convert these with any character you want, it's optionnal but better looking

B. Maze display
- print_maze()

C. Input handling
- get_key()   
  Some help:  
  - `keyboard.read_event()` will wait for a key event, aka key pressed or released, and return it
  - `event_type` attribute on a keyboard event will tell you what kind of event it is
  - `name` attribute will tell you what key has triggered the event  
    You can use it like this:
  ```python
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        return event.name     # "w", "a", "up", "left"
- move = convert_key_to_direction(key)  
  *for now, print what is returned in get_key() just to check if it works, the logic comes right after*  
  
D. Player logic
- find_player()
- can_move(player, move)
- move_player(move)
  
E. Victory logic
- find_exit() -> returns tuple of position of exit
- is_end -> cheks if player position is on the exit

F. Game loop

ask for what maze (load_maze function)  

find_exit()
while not victory:  
    print maze  
    read for key (not input)  
    convert key to direction  
    try to move in that direction  
        if you can, move  
    is_end
      if is end, victory becomes true

got to the end of the maze
