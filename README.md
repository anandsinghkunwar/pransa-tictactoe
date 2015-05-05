#Ultimate Tic Tac Toe

##The Game and Rules

The game is a modification of the classic game Tic-Tac-Toe. 
The original game, if played optimally, always ends in a tie game. Not so interesting.
The basic modification is that the playing grid is now a **3x3 grid** which contains a **mini-3x3 grid** inside each cell.  
A cell is claimed by a player as _his_ if he wins the **mini-3x3 grid** contained in it. But the cell in which a player can play is not decided by him, but by the move his opponent makes.  
This makes the game unpredictable and complicated.
A detailed description of the complete rules is available on http://mathwithbaddrawings.com/2013/06/16/ultimate-tic-tac-toe/.

##Tools used

Game is built using **pygame** module in **python** mainly, with AI program written in *C* for more accurate move decision.

##Requirements and Tests

Tested to work on Fedora 64 bit and 32 bit machines.  
You will require **python, gcc** commands and **pygame, sys** modules for python to run this game.

##Play Our AI

Once you have managed to understand the rules and decided to play versus the _computer_, just clone the repository and execute the game.py file.

##About the AI

It implements a _Monte Carlo_ algorithm which runs multiple games and based on outcomes/data decides the move to make.

##Performance of the AI

Submission of the AI on hackerrank saw us reach 6th on the Leaderboard.  
For more: https://www.hackerrank.com/challenges/ultimate-ttt (Submitted by _'vaishious'_)

## Alternate AI

For an alternate AI try out the minimax branch of the repository.  
This AI uses a _Minimax_ algorithm coupled with _Alpha-Beta Pruning_ to find the best path to take in the current game tree.
