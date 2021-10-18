import math

bOriPos = {'br1':57, 'bn1':58, 'bb1':59, 'bq1':60, 'bk1':28, 'bb2': 62, 'bn2':63, 'br2': 64 , 'bp1': 49, 'bp2': 50, 'bp3': 51, 'bp4': 52, 'bp5': 53, 'bp6': 54, 'bp7': 55, 'bp8': 56 }
OriPos = {'r1':1, 'n1':2, 'b1':3, 'q1':4, 'k1':5, 'b2': 6, 'n2':7, 'r2': 8 , 'p1': 9, 'p2': 10, 'p3': 11, 'p4': 12, 'p5': 13, 'p6': 14, 'p7': 15, 'p8': 16 }

takenSquares = []
btakenSquares = []
threats = [] #threats for white (black avail moves)
bthreats = [] #threats for black (white avail moves)

#update the squares taken by each colour
def updateBoardPositionsOnly():
    for i in black.items():
        btakenSquares.append(i[1])
    for i in white.items():
        takenSquares.append(i[1])
def updatethreats(threatset, enemy): #enemy is just colour
    threatset.clear()
    for i in enemy.keys():
        list = availmoves(i)
        if len(list) != 0:
            for i in list:
                threatset.append(i)



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
        #print('checking xplus',xpluscheck)
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
        #print('checking xminus',xminuscheck)
        if getrow(p) != getrow(xminuscheck):
            #print('diff row')
            break
        if getPos(xminuscheck) in ally:
            #print('ally taken')
            break
        elif getPos(xminuscheck) in enemy:
            moves.append(xminuscheck)
            #print('enemy taken')
            break
        else:
            moves.append(xminuscheck)
            #print('appending',xminuscheck)
            continue
    yplusstart = 'start'
    while yplusstart == 'start':
        ypluscheck = ypluscheck + 8
        #print('checking yplus',ypluscheck)
        if ypluscheck > 64 or ypluscheck < 1:
            #print('out of area')
            break
        if getPos(ypluscheck) in ally:
            #print('ally taken')
            break
        elif getPos(ypluscheck) in enemy:
            moves.append(ypluscheck)
            #print('enemy taken')
            break
        else:
            moves.append(ypluscheck)
            #print('appending',ypluscheck)
            continue
    yminusstart = 'start'
    while yminusstart == 'start':
        yminuscheck = yminuscheck - 8
        #print('checking yminus',yminuscheck)
        if yminuscheck > 64 or yminuscheck < 1:
            #print('out of area')
            break
        if getPos(yminuscheck) in ally:
            #print('ally taken')
            break
        elif getPos(yminuscheck) in enemy:
            moves.append(yminuscheck)
            #print('enemy taken')
            break
        else:
            moves.append(yminuscheck)
            #print('appending',yminuscheck)
            continue
    return moves

def bismoves(p, ally, enemy):
    moves = []
    xpluscheck = getPos(p)
    xminuscheck = getPos(p)
    ypluscheck = getPos(p)
    yminuscheck = getPos(p)
    #check avail spaces
    if getrow(p) < getcolumn(p):
        xplives = 8 - getcolumn(p)
    else:
        xplives = 8 - getrow(p)
    if getrow(p) < getcolumn(p):
        xmlives = getrow(p) - 1
    else:
        xmlives = getcolumn(p) - 1
    if 8 - getrow(p) < getcolumn(p) - 1 :
        yplives = 8 - getrow(p)
    else:
        yplives = getcolumn(p) - 1
    if 8 - getcolumn(p) < getrow(p) - 1:
        ymlives = 8 - getcolumn(p)
    else:
        ymlives = getrow(p) - 1
    #print(xplives, xmlives, yplives, ymlives)

    while True:
        xpluscheck = xpluscheck + 9
        #print('checking xplus',xpluscheck)
        if getPos(xpluscheck) > 64 or getPos(xpluscheck) < 1:
            break
        if xplives == 0:
            #print('off row')
            break
        if getPos(xpluscheck) in ally:
            #print('ally taken')
            break
        elif getPos(xpluscheck) in enemy:
            moves.append(xpluscheck)
            #print('enemy taken')
            break
        else:
            moves.append(xpluscheck)
            xplives = xplives - 1
            continue
    bxminusstart = 'starting'
    while bxminusstart == 'starting':
        xminuscheck = xminuscheck - 9
        #print('checking xminus',xminuscheck)
        if getPos(xminuscheck) > 64 or getPos(xminuscheck) < 1:
            break
        if xmlives == 0:
            #print('off row')
            break
        if getPos(xminuscheck) in ally:
            #print('ally taken')
            break
        elif getPos(xminuscheck) in enemy:
            moves.append(xminuscheck)
            #rint('enemy taken')
            break
        else:
            moves.append(xminuscheck)
            #print('appending',xminuscheck)
            xmlives = xmlives - 1
            continue
    byplusstart = 'start'
    while byplusstart == 'start':
        ypluscheck = ypluscheck + 7
        #print('checking yplus',ypluscheck)
        if ypluscheck > 64 or ypluscheck < 1:
            #print('out of area')
            break
        if yplives == 0:
            #print('diff row')
            break
        if getPos(ypluscheck) in ally:
            #print('ally taken')
            break
        elif getPos(ypluscheck) in enemy:
            moves.append(ypluscheck)
            #print('enemy taken')
            break
        else:
            moves.append(ypluscheck)
            #print('appending',ypluscheck)
            yplives = yplives - 1
            continue
    byminusstart = 'start'
    while byminusstart == 'start':
        yminuscheck = yminuscheck - 7
        #print('checking yminus',yminuscheck)
        if yminuscheck > 64 or yminuscheck < 1:
            #print('out of area')
            break
        if ymlives == 0:
            #print('diff row')
            break
        if getPos(yminuscheck) in ally:
            #print('ally taken')
            break
        elif getPos(yminuscheck) in enemy:
            moves.append(yminuscheck)
            #print('enemy taken')
            break
        else:
            moves.append(yminuscheck)
            #print('appending',yminuscheck)
            ymlives = ymlives -1
            continue
    return moves

def kmoves(p, ally, enemy):
    p = getPos(p)
    smoves = [ p+10, p+17, p+15, p+6 , p-10, p-17, p-15, p-6]
    lmoves = []
    moves = []

    if getcolumn(p) > 1:
        lmoves.append(smoves[2])
        lmoves.append(smoves[5])
        if getcolumn(p) > 2:
            lmoves.append(smoves[3])
            lmoves.append(smoves[4])
    if getcolumn(p) < 8:
        lmoves.append(smoves[1])
        lmoves.append(smoves[-2])
        if getcolumn(p) < 7:
            lmoves.append(smoves[0])
            lmoves.append(smoves[-1])

    for i in lmoves:
        if i not in ally and i>0 and i<65:
            moves.append(i)


    return moves


characters = ['p' , 'r' , 'n' , 'b', 'q', 'k' ] #for i in OriPos , i[2]

#get position of piece
def getPos(p):
    if type(p) == int:
        return p
    try:
        return int(black.get(p))
    except:
        return int(white.get(p))

#get row, column of piece
def getrow(piece):
    pos = getPos(piece)
    return int(math.ceil(pos / 8))
def getcolumn(piece):
    pos = getPos(piece)
    a = int(pos % 8)
    if a == 0:
        return 8
    else:
        return a

#avail moves for pieces
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
            for i in rookmoves(p, btakenSquares, takenSquares):
                moves.append(i)
        else: #white rook
            for i in rookmoves(p, takenSquares, btakenSquares):
                moves.append(i)
    if x == 2: #knight
        if p[0] == 'b':
            for i in kmoves(p, btakenSquares, takenSquares):
                moves.append(i)
        else:
            for i in kmoves(p, takenSquares, btakenSquares):
                moves.append(i)
    if x == 3: #bishop
        if p[0] == 'b':
            if p[1] == 'b': #black bishop
                for i in bismoves(p, btakenSquares, takenSquares):
                    moves.append(i)
            else:
                for i in bismoves(p, takenSquares, btakenSquares):
                    moves.append(i)
    if x == 4: #queen
        if p[0] == 'b':
#            moves.append(rookmoves(p, btakenSquares, takenSquares))
#            moves.append(bismoves(p, btakenSquares, takenSquares))
            r = rookmoves(p, btakenSquares, takenSquares)
            b = bismoves(p, btakenSquares, takenSquares)
            for i in r:
                moves.append(i)
            for i in b:
                moves.append(i)
        else:
            r = rookmoves(p, takenSquares, btakenSquares)
            b = bismoves(p, takenSquares, btakenSquares)
            for i in r:
                moves.append(i)
            for i in b:
                moves.append(i)

    if x == 5: #king
        if p[0] == 'b': #black king, enemy is white
            updatethreats(bthreats, white)
            tmoves = []
            pos = getPos(p)
            if getcolumn(p) >= 2:
                tmoves.append(pos+7)
                tmoves.append(pos-1)
                tmoves.append(pos-9)
            if getcolumn(p) <= 7:
                tmoves.append(pos+9)
                tmoves.append(pos+1)
                tmoves.append(pos-7)
            tmoves.append(pos+8)
            tmoves.append(pos-8)
            for i in tmoves:
                if i >= 1 and i <= 64 and i not in btakenSquares and i not in bthreats:
                    moves.append(i)
#            print(bthreats)



    return moves

print(availmoves('bk1'))
#print(availmoves('r1'))
