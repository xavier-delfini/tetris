piece=[[0,0,0],[0,0,0],[0,0,1]]
m=0
if piece[m][0] + piece[m][1] + piece[m][2] == 0:
    piece.pop(m)
print (piece)