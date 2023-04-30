from itertools import product

files = ["a", "b", "c", "d", "e", "f", "g", "h"]
ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]
promotion = ["Q", "R", "B", "N"]

# gets an upper bound for the UCI vocab

with open("data/UCIvocab.txt", "w") as f:
    for file1, rank1, file2, rank2 in product(files, ranks, files, ranks):
        if file1 == file2 and rank1 == rank2:
            continue 
        if rank2 == "8" and rank1 == "7" or rank2 == "1" and rank1 == "2":
            idx1 = files.index(file1)
            idx2 = files.index(file2)
            if abs(idx1 - idx2) > 1:
                continue
            for promotion_piece in promotion:
                f.write(f'{file1}{rank1}{file2}{rank2}{promotion_piece}\n') 
        f.write(f'{file1}{rank1}{file2}{rank2}\n')

f.close() 



