T_Block = [[0, 6, 0],
           [6, 6, 6],
           [0, 0, 0]]
Line = [[0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]]
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

"""
def rotation(array_piece):
    piece = array_piece[0]
    rotation_count = array_piece[1]
    i = 0
    match len(piece[0]):
        # L reverseL,S_Block,Z_block
        case 3:
            while i < rotation_count:
                new_piece = [[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]]
                new_piece[0] = [piece[2][0], piece[1][0], piece[0][0]]
                new_piece[1] = [piece[2][1], piece[1][1], piece[0][1]]
                new_piece[2] = [piece[2][2], piece[1][2], piece[0][2]]
                piece = new_piece
                i += 1
            if rotation_count < 4:
                rotation_count += 1
            else:
                rotation_count = 1
        # Line
        case 4:
            while i < rotation_count:
                new_piece = [[0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]]
                new_piece[0] = [0, piece[2][0], piece[1][0], 0]
                new_piece[1] = [piece[3][1], piece[2][1], piece[1][1], piece[0][1]]
                new_piece[2] = [piece[0][2], piece[2][2], piece[1][2], piece[3][2]]
                new_piece[3] = [0, piece[2][3], piece[1][3], 0]
                piece = new_piece
                i += 1
            if rotation_count < 2:
                rotation_count += 1
            else:
                rotation_count = 1

    return piece, rotation_count


def hitbox_affinate(hitbox):
    m = 0
    match len(hitbox):
        case 1: pass
        case 2:
            pass
        case 3:
            while m < len(hitbox):

                try:
                    if hitbox[m][0] + hitbox[m][1] + hitbox[m][2] == 0:
                        hitbox.pop(m)
                        m = 0

                    elif hitbox[0][m] + hitbox[1][m] + hitbox[2][m] == 0:
                        del hitbox[0][m], hitbox[1][m], hitbox[2][m]
                        m = 0
                except IndexError:
                    pass
                m += 1

        case 4:
            if hitbox == [1,1,1,1]:
                pass
            else:
                if (all(hitbox[0])) or (all(hitbox[1])):
                    hitbox = [1, 1, 1, 1]
                else:
                    hitbox=[[1], [1], [1], [1]]
    return hitbox


print(hitbox_affinate(rotation([Line, 2])[0]))
def draw_pieces(d_piece, position):
    d_piece=hitbox_affinate(d_piece)
    if position is None:
        position = [-1, -1]

    j = position[1]
    for x in d_piece:
        i = position[0]
        try:
            for y in x:
                #width, height = calc_position_grid([i, j])
                if y > 0:
                    print(y)
                    #color = color_selector(y)
                    #pygame.draw.rect(window, color, ((width, height), (22, 22)), 0)
                    #pygame.display.flip()
                i += 1
        except TypeError:
            #width, height =calc_position_grid([i,j])
            if x > 0:
                print(x)
                #color = color_selector(x)
                #pygame.draw.rect(window, color, ((width, height), (22, 22)), 0)
                #pygame.display.flip()
            i += 1
        j += 1
draw_pieces(hitbox_affinate(rotation([Line, 1])[0]),[2,0])"""
n = 0
grid_array = []
while n < 22:
    grid_array.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    n += 1
grid_array[21]=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
grid_array[2]=[1,2, 1, 2, 1, 2, 3, 4, 5, 6]
grid_array[3]=[1,2, 1, 2, 1, 2, 3, 4, 5, 6]
grid_array[15]=[1,2, 1, 2, 1, 2, 3, 4, 5, 6]

def check_array(grid_array):
    def all_positive(line):
        return all(x > 0 for x in line)
    count=0
    i=0
    for line in grid_array:
        if all_positive(line)==True:
            del grid_array[i]
            grid_array.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            count +=1
        i+=1
    match count:
        case 1:
            score = 1
        case 2:
            score = 3
        case 3:
            score = 5
        case 4:
            score = 8
        case _:
            score = 0
    print(count)
    return grid_array
print(check_array(grid_array))