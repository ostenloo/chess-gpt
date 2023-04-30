from stockfish import Stockfish

stockfish = Stockfish(path="/Users/austinliu/Stockfish/src/stockfish")

stockfish.set_fen_position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

print(stockfish.get_top_moves(3))