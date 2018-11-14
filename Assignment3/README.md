#CS 520: Assignment 3 - Probabilistic Search (and Destroy) 
####16:198:520 Due Nov 18 by Midnight
* flat     : terrain = 1  P = 0.2  WHITE    
* hill     : terrain = 2  P = 0.3  GREY
* forest   : terrain = 3  P = 0.3  GREEN
* cave     : terrain = 4  P = 0.2  DARKGREY


#### 第二题思路
* 没用到neighourhood点？ 
* 比较两个概率：点不在search点的概率        和 点在search点却找不到的概率
* 对应的策略：  平均分配with [type1,type2] 和 把search点的概率给到neighourhood点 with [type1,type2]
* 基于第一轮瞎几把猜 明显是第一个概率比较大 故认为第一个方法更合适