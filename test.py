T_Block = [[0, 6, 0],
           [6, 6, 6],
           [0, 0, 0]]
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
n = 9001
def main(n):


    x=increment(n)
    print (x)
    print (n)


def increment(x):
    x += 1
    return x

main(n)