moves = set() 

with open("data/PGNVocab.txt", "r") as f: 
    lines = f.readlines() 
    for line in lines: 
        moves.add(line.strip("+#\n"))

f.close() 

with open("data/PGNVocabStrip.txt", "w") as f: 
    for move in moves: 
        f.write(move + "\n")