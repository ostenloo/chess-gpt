black_games = []
white_games = [] 

file_names = ["tal_black_games", "tal_white_games"]

for file in file_names:
    with open(f"data/{file}.pgn", 'r') as f: 
        lines = f.readlines() 
        game = ""
        for line in lines[0:100]: 
            game += line.strip("\n") + " "
            if line == "\n": 
                moves = game.split(" ")
                game = line.strip("\n") + " "
                black_games.append(moves)

    f.close()  