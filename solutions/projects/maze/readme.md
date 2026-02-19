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
  - If you add `suppress=True` in the parameters of `read_event()`, this will prevent you from typing anywhere, and will simply read without typing the characters
  - `event_type` attribute on a keyboard event will tell you what kind of event it is, for example `KEY_UP` or `KEY_DOWN`
  - `name` attribute will tell you what key has triggered the event  
    You can use it like this:
  ```python
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        return event.name     # "w", "a", "up", "left"
  ```

- move = convert_key_to_direction(key)  
  This should return a tuple indicating direction to check.  
  Left would be (0, -1), up would be (-1, 0).. (don't forget that matrices are read as `[line][column]`!)  

  *for now, print what is returned just to check if it works, the logic comes right after*

  
  *VERY OPTIONAL: If you don't want to be able to hold the key to move, you should put a `while True` loop, this will make an 'infinite' loop but you can leave it with a return:*
  ```python
  # add a global variable 'pressed' or something 
  # outside the fonction, and global it here

  while True:
    if <key is down> and not pressed:
      pressed = True
      return value
    if <key is up>:
      pressed = False

  # This will make the loop continue until the key is released
  # so the whole script would "stop" until that event
  #
  # Also, the keyboard.read_event() waits for an event instead of
  # testing again and again, so that reduces CPU usage
  ```  
  
D. Player logic
- find_player()
- can_move(move)  
  Checks if it is not outside of the array   
  (false if `x or y < 0` and if `x > size of line` and if `y > size of column`) *Don't forget that an array starts at 0!*  
  Checks if it is not a wall
- move_player(move)  
  Move the player in the maze array
  
E. Victory logic
- find_end() -> returns tuple of position of exit  
  *You could add this in the find_player() logic so you don't have to check twice the array, but that's optional.*
- is_end -> cheks if player position is on the exit

F. Game loop

ask for what maze (load_maze function)  

find where is the player and the end
while not victory:  
    print maze  
    read for key (not input)  
    convert key to direction  
    try to move in that direction ->
        if you can, move and update player position  
    is_end ->
      if is end, victory becomes true

got to the end of the maze
