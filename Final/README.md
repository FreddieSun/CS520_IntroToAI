# Final Exam Note

## Question 1 Localization

### (a)
数点算概率即可

### (b)
**TODO存疑**

### (c)
用proj1 A*算法， 更改迷宫输入即可

### (d)
#### d.1
写代码遍历每个可能的点，计算最后一个状态在当前cell的概率

### d.2
思想类似扫雷算法里的。 算出所有的可能的solution， 然后利用这些solution来算概率。

## Question 2 Markov Decision Processes

为什么会有discount factor？而不是所有原先的数值直接乘以0.9倍 : fixed

思路： 
1. PageRank
2. Value Iteration

* [Value Iteration](https://github.com/aimacode/aima-java)  
* [text book](http://aima.cs.berkeley.edu/)  
* [PageRank详解](https://blog.csdn.net/hguisu/article/details/7996185)  


