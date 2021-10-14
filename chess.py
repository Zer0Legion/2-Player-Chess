#8     bQ bK
#7
#6
#5
#4
#3
#2
#1      Q K
# a b c d e f g h
#x 1 2 3 4 5 6 7 8
import math

bOriPos = {'br1':36, 'bk1':58, 'bb1':59, 'bq':60, 'bk':61, 'bb2': 62, 'bk2':63, 'br2': 64 , 'bp1': 49, 'bp2': 50, 'bp3': 51, 'bp4': 52, 'bp5': 53, 'bp6': 54, 'bp7': 55, 'bp8': 56 }
OriPos = {'r1':38, 'k1':2, 'b1':3, 'q':4, 'k':5, 'b2': 6, 'k2':7, 'r2': 8 , 'p1': 9, 'p2': 10, 'p3': 11, 'p4': 12, 'p5': 13, 'p6': 14, 'p7': 15, 'p8': 16 }

takenSquares = []
btakenSquares = []
def updateBoardPositionsOnly():
    for i in black.items():
        btakenSquares.append(i[1])
    for i in white.items():
        takenSquares.append(i[1])


black = bOriPos
white = OriPos
updateBoardPositionsOnly()

def rookmoves(p, ally, enemy):
    moves = []
    xpluscheck = getPos(p)
    xminuscheck = getPos(p)
    ypluscheck = getPos(p)
    yminuscheck = getPos(p)
    while True:
        xpluscheck = xpluscheck + 1
        print('checking xplus',xpluscheck)
        if getrow(p) != getrow(xpluscheck):
            break
        if getPos(xpluscheck) in ally:
            break
        elif getPos(xpluscheck) in enemy:
            moves.append(xpluscheck)
            break
        else:
            moves.append(xpluscheck)
            continue
    xminusstart = 'starting'
    while xminusstart == 'starting':
        xminuscheck = xminuscheck - 1
        print('checking xminus',xminuscheck)
        if getrow(p) != getrow(xminuscheck):
            print('diff row')
            break
        if getPos(xminuscheck) in ally:
            print('ally taken')
            break
        elif getPos(xminuscheck) in enemy:
            moves.append(xminuscheck)
            print('enemy taken')
            break
        else:
            moves.append(xminuscheck)
            print('appending',xminuscheck)
            continue
    yplusstart = 'start'
    while yplusstart == 'start':
        ypluscheck = ypluscheck + 8
        print('checking yplus',ypluscheck)
        if ypluscheck > 64 or ypluscheck < 1:
            print('out of area')
            break
        if getPos(ypluscheck) in ally:
            print('ally taken')
            break
        elif getPos(ypluscheck) in enemy:
            moves.append(ypluscheck)
            print('enemy taken')
            break
        else:
            moves.append(ypluscheck)
            print('appending',ypluscheck)
            continue
    yminusstart = 'start'
    while yminusstart == 'start':
        yminuscheck = yminuscheck - 8
        print('checking yminus',yminuscheck)
        if yminuscheck > 64 or yminuscheck < 1:
            print('out of area')
            break
        if getPos(yminuscheck) in ally:
            print('ally taken')
            break
        elif getPos(yminuscheck) in enemy:
            moves.append(yminuscheck)
            print('enemy taken')
            break
        else:
            moves.append(yminuscheck)
            print('appending',yminuscheck)
            continue
    return moves

characters = ['p' , 'r' , 'k' , 'b', 'q', 'k' ] #for i in OriPos , i[2]

#get position of piece is Pos.get(' (piece) ')

def getPos(p):
    if type(p) == int:
        return p
    try:
        return int(black.get(p))
    except:
        return int(white.get(p))

def getrow(piece):
    pos = getPos(piece)
    return int(math.ceil(pos / 8))

def availmoves( p ):
    moves = []
    pieceType = p[-2]
    x = characters.index(pieceType) #character identifier
    if x == 0: #pawn
        if p[0] == 'b': #black pawn
            if getrow(p) == 7 : #move double
                if (getPos(p)-16) not in takenSquares:
                    moves.append( getPos(p)-16 )
            moves.append(getPos(p)-8 )
            pawneat = [getPos(p) - 9 , getPos(p) - 7 ]
            for i in pawneat:
                if i in takenSquares and getrow(i) == getrow(p) - 1:
                    moves.append(i)
            for i in moves:
                if i in btakenSquares:
                    moves.remove(i)

        elif p[0] == 'p': #white pawn
            if getrow(p) == 2 : #move double
                if getPos(p)+16 not in btakenSquares:
                    moves.append( getPos(p)+16 )
            moves.append(getPos(p)+8 )
            pawneat = [getPos(p) + 7 , getPos(p) + 9 ]
            for i in pawneat:
                if i in btakenSquares and getrow(i) == getrow(p) + 1:
                    moves.append(i)
            for i in moves:
                if i in takenSquares:
                    moves.remove(i)

    if x == 1: #rook
        if p[0] == 'b': #black rook

            moves.append(rookmoves(p, btakenSquares, takenSquares))
        else: #white rook
            moves.append(rookmoves(p, takenSquares, btakenSquares))


#    if x == 2: #knight
#    if x == 3: #bishop
#    if x == 4: #queen
#    if x == 5: #king
    return moves

#print('getpos',getPos('p8'))
#print('getrow', getrow('p8'))
print('availmoves', availmoves('r1'))
#print('black positions:', btakenSquares)


#print(getPos('p8'))
