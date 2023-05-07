import os 

ddp_rank = int(os.environ['RANK'])

print(ddp_rank)