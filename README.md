# Voltorb Flip

## How to Use

Read the numbers down the right-side and input them all on one line. That means the line alternates between coins and voltorb counts.

Then do the same with the bottom, now reading down-left. This means the line still alternates between coins and voltorb counts, from left to right.

After that moves will be given, in the format `(r, c) safety multiplier`. The first item is the cell to play, 1-indexed, the first number being the row and the second being the column.

The second number is a score of how safe the move is, out of 1. The third number is how likely the move is to give a multiplier, out of 1.

After you play the move, you must input the number you received. If you lost the game, quit the program.

If you run into any errors, double-check your input list.

## How it Works

The code essentially runs a recursive-backtracking algorithm, trying to fill in cells and backtracking when restrictions aren't met.
