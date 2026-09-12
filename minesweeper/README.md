# Minesweeper

An AI that plays Minesweeper by building a knowledge base of logical sentences about
the board and inferring which cells are safe or contain mines.

## Usage

```
pip install -r requirements.txt
python runner.py
```

Click a cell to reveal it, or right-click to flag it as a mine. "AI Move" lets the
agent take a turn: it plays a cell it knows to be safe, or picks randomly among the
remaining unknowns if it has nothing to go on.

## How it works

Each revealed cell produces a sentence of the form `{cells} = count` — the set of its
unknown neighbours, and how many of them are mines. Two rules drive the inference:

- If a sentence's count equals its number of cells, every cell is a mine. If the
  count is zero, every cell is safe.
- If one sentence's cells are a subset of another's, subtracting them yields a new
  sentence: `B - A = B.count - A.count`.

Conclusions cascade, since marking a cell removes it from every other sentence and
adjusts the counts. The engine therefore loops over both rules until a full pass
produces nothing new, reaching a fixed point before the agent commits to a move.

## Implementation notes

- `minesweeper.py` — `Minesweeper` (game state), `Sentence` (a single logical
  statement), and `MinesweeperAI` (the knowledge base and inference engine).
- `runner.py` — Pygame interface; course-distributed assets are excluded.
- New sentences filter out already-known cells before being added, so the knowledge
  base stays small and empty sentences are pruned each pass.
- The AI flags mines but can't always win: when no safe move is known it must guess,
  which is a limitation of the game rather than the inference.