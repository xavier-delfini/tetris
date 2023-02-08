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
"""
def collision(piece):
    m=-1
    match len(piece):
        case 3:
            while m<len(piece):

                if piece[m][0]+piece[m][1]+piece[m][2] ==0:
                    piece.pop(m)
                    m=0
                m += 1

        case 4:
            while m < len(piece):

                if piece[m][0] + piece[m][1] + piece[m][2]+ piece[m][3] == 0:
                    piece.pop(m)
                    m=0
                m += 1
    return piece

print(collision(T_Block))