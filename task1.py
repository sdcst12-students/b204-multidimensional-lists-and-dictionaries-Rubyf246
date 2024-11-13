#!python3

# data from
# Advanced Dungeons and Dragons Dungeon Masters Guide p74 Cleric Table
# https://s3.amazonaws.com/arena-attachments/804915/348b48a0cbd967122dcb76f5cc6f5a01.pdf
"""
This list of lists contains Table 1a Attack Matrix for Clerics, Druids and Monks 
The index specifies the level of the character, and the entry within the row specifies the 
target to hit Armor Class with 10 on the far left, and -10 on the far right.

Write a function that finds the target based on the level and the armor class
Check the assertion tests for expected output.

Note that this could also be done with a single list and a formula to modify the list content!
"""

table = [
    [],
    [10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25],
    [10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25],
    [10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25],
    [8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23],
    [8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23],
    [8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23],
    [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21],
    [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21],
    [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21],
    [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20],
    [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20],
    [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20],
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20],
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20],
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    [-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
]

def target(lvl,ac):
    op_ac = 10 - ac
    #print (op_ac)
    return table[lvl][op_ac]

def main():
    assert target(5,7) == 11
    assert target(10,-10) == 20
    assert target(17,-3) == 13
    
if __name__ == "__main__":
    main()