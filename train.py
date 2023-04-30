import torch 
import torch.nn as nn 
import chess 
import chess.pgn 

from model import ChessGPT, ChessGPTConfig, Block, MLP, CausalSelfAttention, LayerNorm 

def load_fen_moves(file_name): 
    with open(f"data/{file_name}_fen.txt", 'r') as f: 
        lines = f.readlines() 
        games = []
        for line in lines: 
            games.append(line.strip("\n").split(";")[:-1])
    f.close() 
    return games

def load_pgn_moves(file_name): 
    pass

def load_uci_vocab(): 
    vocab = open("data/UCIVocab.txt", 'r')

    vocab_set = {} 
    for line in vocab.readlines():
        vocab_set.add(line.strip("\n"))

    return vocab_set 

def load_uci_moves(file_name): 
    pgn = open(f"data/{file_name}.pgn", 'r')
    games = [] 

    while True: 
        game = chess.pgn.read_game(pgn)
        if game is None: 
            break
        board = game.board() 
        moves = []
        for move in game.mainline_moves(): 
            moves.append(move)
        games.append(moves)
    
    return games 
            
if __name__ == "__main__": 
    files = ["tal_black_games", "tal_white_games"]
    uci_vocab = load_uci_vocab()
    games_by_color = dict()
    for file in files: 
        color = file.split("_")[1]
        games_by_color[file] = load_uci_moves(file)
    
    vocab_size = 131072
    n_embd = 768 

    embedding = nn.Embedding(vocab_size, n_embd)

    for (color, game) in games_by_color.items(): 
        

    


        
        



