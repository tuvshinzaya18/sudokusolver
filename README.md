# sudokusolver
C program to solve sudoku 

Creater: Tuvshinzaya Erdenekhuu
Goal: Solve simple sudoku
Programming language: C 
 

Simple explanation of code: Program designed solve sudoku by creating lists to keep track of numbers missing for each column, row and 3x3 box. Then for each cell find corresponding column, row and box's missing number set then find intersection of all 3 sets. If size of the resulting set is 1, then put that only member as a correct number for that cell. Then repeat this for all empty cell for necassary amount of time to solve sudoku. In order to avoid infinite loop, if program runs whole cycle for all empty cell without making any change, program will stop and inform user about this. 