# Knights

Solves "Knights and Knaves" logic puzzles — where knights always tell the truth and
knaves always lie — by encoding each puzzle in propositional logic and checking
entailment by model enumeration.

## Usage

```
python puzzle.py
```

No arguments. Each puzzle's knowledge base is defined in `puzzle.py`; the program
prints what can be deduced about every character.

## How it works

Each character gets two symbols, `XKnight` and `XKnave`. A knowledge base holds the
rules of the game — everyone is exactly one kind — plus one biconditional per
statement made: `Biconditional(XKnight, claim)`, read as "X is a knight exactly when
what X said is true". That single form covers both cases, since a knave's claim must
then be false.

`model_check` enumerates every truth assignment over the symbols, discards those in
which the knowledge base is false, and reports a symbol only if it holds in every
surviving model. Statements about statements nest — one biconditional inside another —
so no extra machinery is needed for puzzle 3.

## Implementation notes

- `puzzle.py` — symbol definitions and the four knowledge bases.
- `logic.py` — `Sentence` subclasses (`Symbol`, `Not`, `And`, `Or`, `Implication`,
  `Biconditional`), each with `evaluate`, `formula`, and `symbols`, plus the
  `model_check` entailment routine.

Model checking is exponential in the number of symbols, but with six symbols the
search space is only 64 models, so exhaustive enumeration is fine here.