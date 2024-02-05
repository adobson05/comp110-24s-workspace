""" Ex02 One Shot Battleship."""
__author__ = "730643442"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2
row_guess: int = int(input("Guess a row:"))
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
row_counter: int = 1


while row_guess > grid_size or row_guess < 1:   #checks correct row input
    row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again:"))

column_guess: int = int(input("Guess a column:"))   ##checks correct column input
while column_guess > grid_size or column_guess < 1:
    column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again:"))

if row_guess == secret_row and column_guess == secret_column:
    result_box = "\U0001F7E5"
else:
    result_box = "\U00002B1C"

while row_counter <= grid_size:   #creates and prints grid map
    grid_picture: str = ""
    column_counter: int = 1
    if row_guess == row_counter:  
        while column_counter <= grid_size:
            if column_guess == column_counter:
                grid_picture += result_box
            else: 
                grid_picture += BLUE_BOX
            column_counter += 1
    else:
        while column_counter <= grid_size:
            grid_picture += BLUE_BOX 
            column_counter += 1 
    row_counter += 1
    print(grid_picture)


if row_guess == secret_row and column_guess == secret_column:   #checks for hit or miss
    print("Hit!")
elif row_guess == secret_row and column_guess != secret_column:
    print("Close! Correct row, wrong column.")
elif column_guess == secret_column and row_guess != secret_row:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")