#CS 520: Assignment 3 - Probabilistic Search (and Destroy) 
####16:198:520 Due Nov 18 by Midnight
* flat     : terrain = 1  P = 0.2  WHITE    
* hill     : terrain = 2  P = 0.3  GREY
* forest   : terrain = 3  P = 0.3  GREEN
* cave     : terrain = 4  P = 0.2  DARKGREY
## Environment
* Python 3.7(no extra library) 
##### How to run our program?
1. Run *ProbSearch.py*  
    * You should input 1 or 2 to decide which question to run.

2. In question 1
    * You need to chose a rule. Using Rule1 or Rule2, you will get the result for question 3);
Rule3 and Rule 4 are corresponding to question 4).
    * First it will show where the target locates and what terrain type this cell is. 
 This information is for debug usage, not for the computer running this program. Then it will pop up couple of instructions line by line, which shows what cell it will explore next. 
 Until it finds the target. At the end line, it will show the location and terrain type of the target cell, '
 as well as the number of searches.
3. In question 2
    * The same to procedure 2, chose a rule.
    * First it will show where the target locates and what terrain type this cell is. 
    Then it will pop up couple of instructions line by line, which shows what cell it will explore next and
    where the target moves, as well as the terrain types that the target moves between.
    However, the knowledge base only contains the probabilities of each cell and 
    the terrain types the target moves between.
    * Finally, when the target is found, it will also show the number of total actions
    and total number of searches.
    

