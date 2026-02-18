maze[0] is just an empty square to test moves
next ones are mazes

A. Maze loading
- load_maze(file_path)
  choose what maze (pick the 1st one, and later on modify it so the user can choose it)
- convert_symbols(maze)
  By default, you'll have from 0 to 3:
  - 0 is empty case
  - 1 is wall
  - 2 is player
  - 3 is end  
  Convert these with any character you want, it's optionnal but better looking

B. Maze display
- print_maze(maze)

C. Player logic
- find_player(maze)
- move_player(maze, direction)
- can_move(maze, x, y)

D. Input handling
- get_key() ->   
  event = keyboard.read_event()  
  if event.event_type == keyboard.KEY_DOWN  
    return event.name       # "w", "q", "up", "left"..
- convert_key_to_direction(key)

E. Game loop

ask for what maze (load_maze function)  

while not on the end:  
    print maze  
    read for key (not input)  
    convert key to direction  
    try to move in that direction  
        if you can, move  

got to the end of the maze
