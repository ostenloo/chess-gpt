import chess 
import chess.pgn 

file_names = ["tal_black_games", "tal_white_games"]

for file in file_names:
    pgn = open(f"data/{file}.pgn", 'r')

    fen_file = open(f"data/{file}_fen.txt", 'w') 

    while True: 
        game = chess.pgn.read_game(pgn)
        if game is None: 
            break
        board = game.board() 
        for move in game.mainline_moves(): 
            board.push(move) 
            fen_file.write(board.fen() + ";") 
        fen_file.write("\n")

    pgn.close()
    fen_file.close()
    