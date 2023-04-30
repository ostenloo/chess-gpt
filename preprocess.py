file_path = "data/Tal.pgn"

# save the games based on if tal played white or black
games = {
    "white": [], 
    "black": []
}

with open(file_path) as f: 
    lines = f.readlines() 
    tal_color = None 
    on_pgn_line = False  
    pgn = ""
    for line in lines:
        if on_pgn_line:
            if line.startswith("[Event"): 
                on_pgn_line = False 
                games[tal_color].append(pgn)
                pgn = ""
            else: 
                pgn += line 
        if line.startswith("[White "): 
            player_white = line.split('"')[1]
            if player_white == "Tal, Mihail":
                tal_color = "white"
        elif line.startswith("[Black "):
            player_black = line.split('"')[1]
            if player_black == "Tal, Mihail":
                tal_color = "black"
        elif line.startswith("1."): 
            on_pgn_line = True 
            pgn += line 
        else: 
            # print(tal_color)
            continue 


f.close()  

with open("data/tal_white_games.pgn", "w") as f: 
    for game in games["white"]:
        f.write(game)

f.close()

with open("data/tal_black_games.pgn", "w") as f:
    for game in games["black"]:
        f.write(game)

f.close()