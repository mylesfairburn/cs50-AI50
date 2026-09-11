# Degrees

Finds the shortest path between two actors through shared movies — the "six degrees
of Kevin Bacon" problem — using breadth-first search over an IMDb dataset.

## Usage

```
python degrees.py [directory]
```

`directory` holds `people.csv`, `movies.csv`, and `stars.csv` (defaults to `large`).
Enter two names when prompted; the program prints the chain of movies and actors
connecting them, or "Not connected."

```
Name: Tom Cruise
Name: Kevin Bacon
1 degrees of separation.
1: Tom Cruise and Kevin Bacon starred in A Few Good Men
```

## How it works

BFS on an implicit graph — actors are nodes, shared movies are edges — so the first
path found to the target is guaranteed shortest. Each node stores a parent pointer
and the connecting movie, allowing the full chain to be reconstructed on success.

## Implementation notes

- `degrees.py` — data loading and the `shortest_path` BFS.
- `util.py` — `Node` and frontier classes, backed by a `deque` and a membership
  `set` for O(1) queue operations so the search scales to the ~1M-person dataset.
