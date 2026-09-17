# Crossword

Generates filled crossword puzzles by treating the grid as a **constraint satisfaction problem (CSP)**. Project 3 (Optimization) of CS50 AI.

## Usage

```
pip install pillow
python generate.py data/structure1.txt data/words1.txt [output.png]
```

- `structure` is a grid file where `_` is a fillable cell and `#` is a blocked cell.
- `words` is a newline-separated vocabulary.
- `output` is optional. If you give one, the program also saves the puzzle as an image.

## How it works

Each run of across or down cells is a **variable**, and its **domain** is the set of words that could fill it.

| Step | Method | What it does |
|------|--------|--------------|
| Node consistency | `enforce_node_consistency` | Removes words whose length doesn't match the slot |
| Arc consistency | `revise`, `ac3` | Removes words that have no compatible letter at an overlap with a neighbouring slot |
| Search | `backtrack` | Recursive backtracking that assigns one slot at a time |
| Variable ordering | `select_unassigned_variable` | Chooses the slot with the fewest remaining words (MRV), breaking ties by most neighbours (degree heuristic) |
| Value ordering | `order_domain_values` | Tries first the word that rules out the fewest options for neighbours (least-constraining value) |
| Constraint check | `consistent` | Words are unique, lengths match, and overlapping letters agree |

## Files

- `generate.py`: the CSP solver (my implementation)
- `crossword.py`: the `Variable` and `Crossword` classes, which parse the grid and compute overlaps (course-provided)
- `data/`, `assets/`: sample structures, word lists and font (course-provided, excluded)