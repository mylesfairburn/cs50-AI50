# Tic-Tac-Toe

An unbeatable tic-tac-toe AI that plays optimally using minimax with alpha-beta
pruning. The computer never loses — it either wins or forces a draw.

## Usage

```
python runner.py
```

A pygame window opens; choose to play as X or O. The AI computes its move for the
current board and plays optimally in response to yours.

## How it works

Minimax over the full game tree — the AI assumes both players play optimally and
picks the move with the best guaranteed outcome, scoring a win as +1, a loss as -1,
and a draw as 0. Alpha-beta pruning skips branches that cannot affect the result,
cutting the nodes searched without changing the chosen move.

## Implementation notes

- `tictactoe.py` — game logic (`player`, `actions`, `result`, `winner`, `terminal`,
  `utility`) and the `minimax` search with alpha-beta pruning.
- `runner.py` — the pygame GUI (provided by the course).
- Boards are copied per move so the search never mutates the real game state.