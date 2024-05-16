# Othello Game in Python

This repository contains a Python implementation of the classic strategy board game Othello, also known as Reversi. Othello is played on an 8×8 uncheckered board where two players compete to control the most territory by flipping their opponent's pieces.

## Features

- **Two-Player Mode**: Play against the computer using the Alpha-Beta pruning algorithm.
  
- **Game Setup**: The game starts with an initial setup placing two black disks and two white disks at the center of the board.

- **Gameplay**: Players take turns placing one disk on an empty square, with their assigned color facing up. If the placed disk encloses a straight line of the opponent's disks, those disks are flipped over to the player's color.

- **Alpha-Beta Algorithm**: Challenge the computer in single-player mode, where it employs the Alpha-Beta pruning algorithm to make strategic moves.

- **Rules Enforcement**: The game enforces the rules of Othello, ensuring that only legal moves are allowed.

- **End Game Detection**: The game detects when no more legal moves are possible, signaling the end of the game.

- **Win Determination**: At the end of the game, the player with the majority of their color showing on the board wins.

## How to Play

1. Clone the repository to your local machine.
2. Run the Python script to start the game.
3. Choose level (Easy - Medium - Hard).
4. Follow the on-screen instructions to make your moves.
5. Enjoy playing Othello and challenge yourself against the computer's Alpha-Beta algorithm!
