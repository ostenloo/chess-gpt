# idea for chess-gpt 

## Motivation 

* SotA in Chess -- Stockfish
* MCTS, Alpha Beta Pruning, NNUE  

## Related Work 

* Transformers to detect Stylometry in Chess players 
* Transformers to play Chess 
    * Illegal Moves 
    * Stochastic Parrots 
    * Memorize Openings but performs worse in endgames 

## Methods 

* In this paper, we will explore the capabilities and applications of using a Transformer to build a Chess Engine 

* Our approach will use a traditional Chess Engine StockFish to perform MCTS. StockFish comes equipped with a Multilayer Perceptron called NNUE, which is used 
for positional evaluation. 

* In each position, the best move is chosen and played. This is great for SoTA Chess that far exceeds human capabilities. 

* Here, we attempt to perform Cross Attention on a players' games to stylize StockFish to play like an individual player. 

* To measure how closely the engine matches a players' style, we will run the 