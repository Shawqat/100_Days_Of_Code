# my Version
# def print_maze(maze):
#     # TODO: print each row of the maze
#     for row in maze:
#         print(row)

# def find_player(maze):
#     # TODO: loop through the maze and find the position (row, col) of "P"
#     # return row, col
#     for index, row in enumerate(maze):
#         if "P" in row:
#             return (index, row.index("P"))

# def can_move(maze, row, col):
#     # TODO: return True if maze[row][col] is NOT a wall "#"
#     if maze[row][col] != "#" and maze[row][col] != "X":
#         return True
#     return False

# def helper_function(**keys):
#     maze = keys.get("maze", False)
#     player_row = keys.get("player_row", False)
#     player_col = keys.get("player_col", False)
#     player_new_row = keys.get("player_new_row", False)
#     player_new_col = keys.get("player_new_col", False)
#     if player_col == maze[player_row].index("X"):
#         return "You've escaped"
#     if player_new_row != False:
#         if can_move(maze, player_new_row, player_col):
#                 if maze[player_new_row][player_col] == " ":
#                     new_maze = list(maze[player_new_row])
#                     new_maze[player_col] = "P"
#                     new_maze = "".join(new_maze)
#                     maze[player_row] = maze[player_row].replace("P", " ")
#                     maze[player_new_row] = new_maze
#                     print_maze(maze)
#                     return
#                 else:
#                     return "You've Escaped"
#     if player_new_col:
#         if can_move(maze, player_row, player_new_col):
#                 if maze[player_row][player_new_col] == " ":
#                     new_maze = list(maze[player_row])
#                     new_maze[player_new_col] = "P"
#                     new_maze[player_col] = " "
#                     new_maze = "".join(new_maze)
#                     maze[player_row] = new_maze
#                     print_maze(maze)
#                     return
#                 else:
#                     return "You've Escaped"
# def move_player(maze, player_row, player_col, direction):
#     # TODO: calculate new row/col based on direction ("w","a","s","d")
#     # if can_move() to new position, update maze (remove old P, add new P)
#     # return updated player_row, player_col
#     if direction == "w":
#         helper_function(maze=maze, player_row=player_row, player_col=player_col, player_new_row = player_row - 1)
#     elif direction == "s":
#         helper_function(maze=maze, player_row=player_row, player_col=player_col, player_new_row = player_row + 1)
#     elif direction == "a":
#         helper_function(maze=maze, player_row=player_row, player_col=player_col, player_new_col = player_col - 1)
#     elif direction == "d":
#         helper_function(maze=maze, player_row=player_row, player_col=player_col, player_new_col = player_col + 1)
#     else:
#         return "Invalid direction"
# def play_game():
#     maze = [
#         "##########",
#         "#       ##",
#         "#P # ### #",
#         "#    #   #",
#         "#### # ###",
#         "###   ####",
#         "##   #####",
#         "#      X##",
#         "##########"
#     ]

#     print_maze(maze)
#     # TODO: find starting player position
    
#     # TODO: use a while loop:
#     #   - print the maze
#     #   - ask for input (w/a/s/d)
#     #   - move the player
#     #   - check if player reached "X" -> print "You escaped!" and stop loop
#     while True:
#         user_direction = input("Move ( w => up / a => left / s => down / d => right ): ")
#         player_position = find_player(maze)
#         move_player(maze, player_position[0], player_position[1], user_direction)
#         if user_direction == "done":
#             break
# play_game()

# my version with some edits using Ai 
def print_maze(maze):
    """Print each row of the maze."""
    for row in maze:
        print(row)

def find_player(maze):
    """Return (row, col) of the first 'P' found."""
    for r, row in enumerate(maze):
        if "P" in row:
            return r, row.index("P")
    return None  # should never happen in a valid maze

def can_move(maze, row, col):
    """Return True if the cell is not a wall ('#')."""
    return maze[row][col] != "#"

def move_player(maze, row, col, direction):
    """
    Attempt to move the player.
    Returns (new_row, new_col, escaped) where escaped is True if the player reached 'X'.
    """
    # Compute new coordinates
    if direction == "w":
        new_row, new_col = row - 1, col
    elif direction == "s":
        new_row, new_col = row + 1, col
    elif direction == "a":
        new_row, new_col = row, col - 1
    elif direction == "d":
        new_row, new_col = row, col + 1
    else:
        # Invalid direction – treat as no move
        return row, col, False

    # Check bounds (optional, but maze has walls around)
    # Check if the target is a wall
    if not can_move(maze, new_row, new_col):
        print("You crashed into a wall! :D")
        return row, col, False

    # Check if the target is the exit
    if maze[new_row][new_col] == "X":
        # Remove player from old position
        maze[row] = maze[row][:col] + " " + maze[row][col+1:]
        # Optionally place P on X (for visual satisfaction)
        maze[new_row] = maze[new_row][:new_col] + "P" + maze[new_row][new_col+1:]
        return new_row, new_col, True

    # Normal move to an empty space
    if maze[new_row][new_col] == " ":
        # Update maze: clear old P, place new P
        maze[row] = maze[row][:col] + " " + maze[row][col+1:]
        maze[new_row] = maze[new_row][:new_col] + "P" + maze[new_row][new_col+1:]
        return new_row, new_col, False

    # If we reach here, the cell contains something unexpected – ignore
    return row, col, False

def play_game():
    maze = [
        "##########",
        "#       ##",
        "#P # ### #",
        "#    #   #",
        "#### # ###",
        "###   ####",
        "##   #####",
        "#      X##",
        "##########"
    ]

    print_maze(maze)

    # Find starting position
    player_pos = find_player(maze)
    if player_pos is None:
        print("Player not found!")
        return
    row, col = player_pos

    while True:
        direction = input("Move (w/a/s/d, or 'done' to quit): ").strip().lower()

        if direction == "done":
            print("Game ended.")
            break

        row, col, escaped = move_player(maze, row, col, direction)
        print_maze(maze)

        if escaped:
            print("You escaped! Congratulations!")
            break

play_game()