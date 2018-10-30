# MineSweeper Program
* By Weijia Sun, Yi Wu, Xun Tang, Xinyu Lyu 2018/10/28
## Run the program
* The main function in MineSweeper.py is the main entrance of tour program.
* The default board size for Minesweeper is 16 X 30 with nearly 99 mines, which is just the expert difficult level.
And you can generate your own board for test in 16 line of the Minesweeper.py. For example, self.grid = Grid(16, 30, 0.21) means the size of the board is 16 X 30. And the probability of each cell to be a mine is 0.21.
* If you see the final result and want to run the program for another time, you should close the picture of the final 
result because of characteristic of the pygame package.
## What is on screen?
* We print the board information after every judge step.
* We print the information of every judgement step.
* We will print the final result, after finishing the Minesweeping process whether win or fail.
