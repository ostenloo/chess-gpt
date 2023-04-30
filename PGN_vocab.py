pieces = ["K", "Q", "R", "B", "N"] 
pawns = ["a", "b", "c", "d", "e", "f", "g", "h"]
files = ["a", "b", "c", "d", "e", "f", "g", "h"]
ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]

moves = set()

for piece in pieces: 
    for file in files: 
        for rank in ranks: 
            moves.add(f"{piece}{file}{rank}")
            moves.add(f"{piece}{file}{rank}+")
            moves.add(f"{piece}{file}{rank}#")
            moves.add(f"{piece}x{file}{rank}")
            moves.add(f"{piece}x{file}{rank}+")
            moves.add(f"{piece}x{file}{rank}#")
            # 2 pieces can move to the same square 
            if piece == "R" or piece == "N" or piece == "B" or piece == "Q": 
                for rank1 in ranks: 
                    moves.add(f"{piece}{rank1}{file}{rank}")
                    moves.add(f"{piece}{rank1}{file}{rank}+")
                    moves.add(f"{piece}{rank1}{file}{rank}#")
                    moves.add(f"{piece}{rank1}x{file}{rank}")
                    moves.add(f"{piece}{rank1}x{file}{rank}+")
                    moves.add(f"{piece}{rank1}x{file}{rank}#")
                for file1 in files: 
                    moves.add(f"{piece}{file1}{file}{rank}")
                    moves.add(f"{piece}{file1}{file}{rank}+")
                    moves.add(f"{piece}{file1}{file}{rank}#")
                    moves.add(f"{piece}{file1}x{file}{rank}")
                    moves.add(f"{piece}{file1}x{file}{rank}+")
                    moves.add(f"{piece}{file1}x{file}{rank}#")
                # if there are 3 pieces due to promotion, need to specify file and rank 
                for rank1 in ranks: 
                    for file1 in files: 
                        moves.add(f"{piece}{file1}{rank1}{file}{rank}")
                        moves.add(f"{piece}{file1}{rank1}{file}{rank}+")
                        moves.add(f"{piece}{file1}{rank1}{file}{rank}#")
                        moves.add(f"{piece}{file1}{rank1}x{file}{rank}")
                        moves.add(f"{piece}{file1}{rank1}x{file}{rank}+")
                        moves.add(f"{piece}{file1}{rank1}x{file}{rank}#")

for (idx, pawn) in enumerate(pawns): 
    for rank in ranks[1:6]: #2,3,4,5,6,7
        # pawn pushes 
        if rank == "7": 
            for piece in pieces[1:]: 
                moves.add(f"{pawn}{str(int(rank)+1)}={piece}")
                moves.add(f"{pawn}{str(int(rank)+1)}={piece}+")
                moves.add(f"{pawn}{str(int(rank)+1)}={piece}#")
        elif rank == "2":
            for piece in pieces[1:]: 
                moves.add(f"{pawn}{str(int(rank)-1)}={piece}")
                moves.add(f"{pawn}{str(int(rank)-1)}={piece}+")
                moves.add(f"{pawn}{str(int(rank)-1)}={piece}#")  
        else: 
            moves.add(f"{pawn}{str(int(rank)+1)}")
            moves.add(f"{pawn}{str(int(rank)+1)}+")
            moves.add(f"{pawn}{str(int(rank)+1)}#")
            moves.add(f"{pawn}{str(int(rank)-1)}")
            moves.add(f"{pawn}{str(int(rank)-1)}+")
            moves.add(f"{pawn}{str(int(rank)-1)}#")
        # pawn captures 
        if pawn == "a": 
            if rank == "7": 
                for piece in pieces[1:]: 
                    moves.add(f"{pawn}xb{str(int(rank)+1)}={piece}")
                    moves.add(f"{pawn}xb{str(int(rank)+1)}={piece}+")
                    moves.add(f"{pawn}xb{str(int(rank)+1)}={piece}#")
            elif rank == "2":
                for piece in pieces[1:]:
                    moves.add(f"{pawn}xb{str(int(rank)-1)}={piece}")
                    moves.add(f"{pawn}xb{str(int(rank)-1)}={piece}+")
                    moves.add(f"{pawn}xb{str(int(rank)-1)}={piece}#")
            else: 
                moves.add(f"{pawn}xb{str(int(rank)+1)}")
                moves.add(f"{pawn}xb{str(int(rank)+1)}+")
                moves.add(f"{pawn}xb{str(int(rank)+1)}#")
                moves.add(f"{pawn}xb{str(int(rank)-1)}")
                moves.add(f"{pawn}xb{str(int(rank)-1)}+")
                moves.add(f"{pawn}xb{str(int(rank)-1)}#")
        elif pawn == "h": 
            if rank == "7":
                for piece in pieces[1:]:
                    moves.add(f"{pawn}xg{str(int(rank)+1)}={piece}")
                    moves.add(f"{pawn}xg{str(int(rank)+1)}={piece}+")
                    moves.add(f"{pawn}xg{str(int(rank)+1)}={piece}#")
            elif rank == "2":
                for piece in pieces[1:]:
                    moves.add(f"{pawn}xg{str(int(rank)-1)}={piece}")
                    moves.add(f"{pawn}xg{str(int(rank)-1)}={piece}+")
                    moves.add(f"{pawn}xg{str(int(rank)-1)}={piece}#")
            else: 
                moves.add(f"{pawn}xg{str(int(rank)+1)}")
                moves.add(f"{pawn}xg{str(int(rank)+1)}+")
                moves.add(f"{pawn}xg{str(int(rank)+1)}#")
                moves.add(f"{pawn}xg{str(int(rank)-1)}")
                moves.add(f"{pawn}xg{str(int(rank)-1)}+")
                moves.add(f"{pawn}xg{str(int(rank)-1)}#")
        else: 
            if rank == "7":
                for piece in pieces[1:]: 
                    moves.add(f"{pawn}{str(int(rank)+1)}={piece}")
                    moves.add(f"{pawn}{str(int(rank)+1)}={piece}+")
                    moves.add(f"{pawn}{str(int(rank)+1)}={piece}#")
                    moves.add(f"{pawn}x{str(int(rank)+1)}={piece}")
                    moves.add(f"{pawn}x{str(int(rank)+1)}={piece}+")
                    moves.add(f"{pawn}x{str(int(rank)+1)}={piece}#")
            elif rank == "2":
                for piece in pieces[1:]: 
                    moves.add(f"{pawn}{str(int(rank)-1)}={piece}")
                    moves.add(f"{pawn}{str(int(rank)-1)}={piece}+")
                    moves.add(f"{pawn}{str(int(rank)-1)}={piece}#")
                    moves.add(f"{pawn}x{str(int(rank)-1)}={piece}")
                    moves.add(f"{pawn}x{str(int(rank)-1)}={piece}+")
                    moves.add(f"{pawn}x{str(int(rank)-1)}={piece}#")
            else: 
                moves.add(f"{pawn}x{pawns[idx-1]}{str(int(rank)+1)}")
                moves.add(f"{pawn}x{pawns[idx-1]}{str(int(rank)+1)}+")
                moves.add(f"{pawn}x{pawns[idx-1]}{str(int(rank)+1)}#")
                moves.add(f"{pawn}x{pawns[idx+1]}{str(int(rank)+1)}")
                moves.add(f"{pawn}x{pawns[idx+1]}{str(int(rank)+1)}+")
                moves.add(f"{pawn}x{pawns[idx+1]}{str(int(rank)+1)}#")
                moves.add(f"{pawn}x{pawns[idx-1]}{str(int(rank)-1)}")
                moves.add(f"{pawn}x{pawns[idx-1]}{str(int(rank)-1)}+")
                moves.add(f"{pawn}x{pawns[idx-1]}{str(int(rank)-1)}#")
                moves.add(f"{pawn}x{pawns[idx+1]}{str(int(rank)-1)}")
                moves.add(f"{pawn}x{pawns[idx+1]}{str(int(rank)-1)}+")
                moves.add(f"{pawn}x{pawns[idx+1]}{str(int(rank)-1)}#")

# add castling         
moves.add("O-O")
moves.add("O-O+")
moves.add("O-O#")
moves.add("O-O-O")
moves.add("O-O-O+")
moves.add("O-O-O#")

with open("data/PGNVocab.txt", "w") as f: 
    for move in moves: 
        f.write(move + "\n")

f.close() 