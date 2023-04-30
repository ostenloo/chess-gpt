import torch 

# x = torch.tensor([1, 2, 3, 4])
# print(x.dim()) # this is not the shape 
# print(torch.unsqueeze(x, 0))
# print(torch.unsqueeze(x, 1))
# # torch.unsqueeze(x, 2) #    torch.unsqueeze(x, 2)
# # IndexError: Dimension out of range (expected to be in range of [-2, 1], but got 2)
# # print(x)
# print(torch.unsqueeze(x, -2))
# print(torch.unsqueeze(x, -1))

# y = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])

# print("no unsqueeze shape", y.shape)

# for dim in range(-y.dim()-1, y.dim()+1): 
#     # print(dim, torch.unsqueeze(y, dim))
#     print(f"dim {dim} shape", torch.unsqueeze(y, dim).shape)

"""
    no unsqueeze shape torch.Size([2, 4])
    dim -3 shape torch.Size([1, 2, 4])
    dim -2 shape torch.Size([2, 1, 4])
    dim -1 shape torch.Size([2, 4, 1])
    dim 0 shape torch.Size([1, 2, 4])
    dim 1 shape torch.Size([2, 1, 4])
    dim 2 shape torch.Size([2, 4, 1])
""" 

# t = 10

# a = torch.arange(0, t, dtype=torch.long)

# print(a.shape)

# b = torch.unsqueeze(a, 0)

# print(b.shape)

# c = b[:,0:9] #tensor([[0, 1, 2, 3, 4, 5, 6, 7, 8]])
# print(c)

# d = b[:, -1] 
# print(d) # tensor([9])

# e = b[:, 9] # tensor([9])
# print(e)

# f = e.unsqueeze(0) # tensor([[9]])
# print(f)

# g = torch.cat((c, f), dim=1)
# print(g) # tensor([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])


# def load_pgn_moves(file_name): 
#     pgn = open(f"data/{file_name}.pgn", "r")
#     games = [] 

#     pgn_content = pgn.read() 

#     games = pgn_content.split("\n\n")[:-1]

#     game_move_list = []

#     for game in games: 
#         moves = [move[max(0,move.find(".")+1):].strip("\n") for move in game.split(" ")[:-2]]
#         print(moves)
#         game_move_list.append(moves)

#     return game_move_list

# game_move_list = load_pgn_moves("tal_white_games")

x = torch.randn(3,2)

print(x)

print(x.contiguous())