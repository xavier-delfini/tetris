T_Block = [[0, 6, 0],
           [6, 6, 6],
           [0, 0, 0]]
Line = [[0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
"""

grid_array=[]
n=0
while n < 22:
    grid_array.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    n += 1

position=[4,0]
def verif_collision(piece,position,grid):
    i=0
    for c in piece[-1]:
        if (grid[position[1]+(1*i)][(position[0]+1)] > 0  and c >0) or position[1]==20:
            position=[4,0]
        i+=1
    return position

while True:
    position=verif_collision(T_Block,position,grid_array)
    position[1]+=1
""""""
test = [0, 1, 2, 3, 4, 5]



def new_piece(test):
    tost=test
    remove(test)
    print(tost)
    print(test)

def remove(test):
    test.remove(3)
    return test


new_piece(test)
"""
n = 0
grid_array = []
while n < 22:
    grid_array.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    n += 1
grid_array[2] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def all_positive(line):
    return all(x > 0 for x in line)


for x in grid_array:
    if all_positive(x) == True:
        print("Une ligne est remplie")
