# sudokusolver
Python program to solve sudoku 

Creater: Tuvshinzaya Erdenekhuu
Goal: Solve simple sudoku
Programming language: Python 
 

Simple explanation of code: Uses 2 step to solve it. (Only uses logical way. No brute force try) 
1. for every boxes. Takes one possible numbers as a target number. Check all possible locations where
target number can be. If there is only 1 possible location, put target value in that location,
2. for every cell. See what numbers it can but by comparing numbers in that row, numbers in that column 
and numbers in that box


Explanation of input:
write each row as a continues number and put 0 in empty cells.
like:
374|168|259    =====>   374168259
519|427|683    =====>   519427683
286|395|714    =====>   286395714 
-----------    =====>   698541372 
698|541|372    =====>   123786945
123|786|945    =====>   457932168
457|932|168    =====>   962874531
-----------    =====>   835619427
962|874|531    =====>   741253896
835|619|427    =====>
741|253|896    =====>
