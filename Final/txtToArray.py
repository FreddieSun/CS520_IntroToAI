import pandas as pd


data=pd.read_table("Maze.txt",header=None)


maze=[]
for i in range(43):
    temp = []
    for j in data.loc[i]:
        temp2 = j
        for j2 in temp2:
            if j2 == 'G':
                temp.append(0)
            else:
                temp.append(int(j2))
    maze.append(temp)

print(maze)
print(len(maze))
print(len(maze[0]))