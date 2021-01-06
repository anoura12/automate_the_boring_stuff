def isValidChessBoard(dictionary):
    pieces = ['pawn','knight','king','queen','bishop','rook'] #an array with all chess pieces 
    counter = {}
    numbers = {}
    i = 0

    #checks the position of each piece
    for positions in dictionary.keys():
        number = positions[0]
        letter = positions[1]
        if(int(number) < 1 or int(number) > 8):
            print("Invalid positon number - " + number)
            i = i + 1
        if(ord(letter) < 97 or ord(letter) > 104):
            print("Invalid position letter - " + letter)
            i = i + 1

    
    #checks the colour and the type of chess piece
    for piece in dictionary.values():
        counter.setdefault(piece,0)
        counter[piece] = counter[piece] + 1
        if("wking" in counter.keys()):
            if(counter['wking'] != 1):
                print("Invalid number of kings")
                i = i + 1

        if("bking" in counter.keys()):
            if(counter['bking'] != 1):
                print("Invalid number of kings")
                i = i + 1        

        if(piece[0] != 'w' and piece[0] != 'b'):
            print("Invalid colour piece")
            i = i + 1

        length = len(piece)
        move = piece[1:length]
        if(move in pieces == False):
            print("Invalid piece - " + move)
            i = i + 1
    while('wpawn' in counter.keys() == True or 'bpawn' in counter.keys() == True):
        if(counter['wpawn'] > 8 or counter['bpawn'] > 8):
            print("Invalid number of pawns")
            i = i + 1
    if(len(counter) > 16):
        print("Invalid number of pieces")
        i = i + 1

    #i is a counter where if anything invalid about the chess pieces pops up, it will increment by one.
    #so if i is 1 or more than 1, it will return false.
    if(i >= 1):
        print("False")
    else:
        print("True")


chess = {'1h': 'wpawn', '6a': 'wqueen', '6a': 'bbishop', '5c': 'bqueen', '3e': 'wking'} #sample chess board

isValidChessBoard(chess)
         
