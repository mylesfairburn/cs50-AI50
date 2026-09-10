# CS50's Introduction to Artificial Intelligence with Python

My project solutions for [CS50 AI](https://cs50.harvard.edu/ai/), covering search,
knowledge representation, uncertainty, optimization, learning, neural networks, and
language.

## Projects

| # | Project | Topic | Key idea |
|---|---------|-------|----------|
| 0 | Degrees | Search | BFS for shortest path between actors via shared films |
| 0 | Tic-Tac-Toe | Search | Minimax with optimal adversarial play |
| 1 | Knights | Knowledge | Model-checking logic puzzles with propositional logic |
| 1 | Minesweeper | Knowledge | Inference engine deducing safe cells |
| 2 | PageRank | Uncertainty | Ranking pages via random-surfer and iterative methods |
| 2 | Heredity | Uncertainty | Bayesian network for gene/trait probabilities |
| 3 | Crossword | Optimization | Constraint satisfaction with backtracking |
| 4 | Shopping | Learning | k-nearest-neighbors purchase prediction |
| 4 | Nim | Learning | Reinforcement learning via Q-learning |
| 5 | Traffic | Neural Networks | CNN for road-sign image classification |
| 6 | Parser | Language | Context-free grammar sentence parsing |
| 6 | Attention | Language | Masked-word prediction with a transformer |

*(Table lists the full course; see individual folders for what's completed.)*

## Structure

Each project lives in its own directory with its source and a brief README. Data
sets and other course-distributed files are excluded.

## Running

Each project is self-contained:

```
cd degrees
pip install -r requirements.txt   # where present
python degrees.py
```

## Note

Solutions are shared for reference. If you're currently taking CS50 AI, please
follow the course's academic honesty policy and write your own.
