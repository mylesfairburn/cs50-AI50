# Nim

An AI that teaches itself to play Nim through reinforcement learning (Q-learning).

## The game

- The board starts as four piles: `[1, 3, 5, 7]`
- Players take turns removing one or more objects from a single pile
- Whoever removes the last object **loses**

## How it works

The AI plays thousands of games against itself and learns a Q-value for each `(state, action)` pair:

- **State:** a tuple of the pile sizes, e.g. `(0, 2, 4, 7)`
- **Action:** `(i, j)`, meaning remove `j` objects from pile `i`
- **Rewards:** `-1` for the move that loses, `1` for the opponent's last move before that, `0` otherwise

After each move, Q-values are updated with:

```
Q(s, a) <- Q(s, a) + alpha * ((reward + best_future_reward) - Q(s, a))
```

During training it uses an **epsilon-greedy** strategy: with probability `epsilon` it tries a random move, and otherwise it plays the best move it knows. When playing against a human it always picks the best move.

## Implemented functions (`nim.py`)

- `get_q_value`: looks up the Q-value for a state and action, returning 0 if it hasn't been seen
- `update_q_value`: applies the Q-learning update formula
- `best_future_reward`: returns the highest Q-value available from a state, or 0 if there are no moves
- `choose_action`: picks the best action, or a random one with probability `epsilon`

## Parameters

| Parameter | Default | Meaning |
|-----------|---------|---------|
| `alpha`   | 0.5     | Learning rate |
| `epsilon` | 0.1     | Chance of exploring with a random move |

## Running

```
python play.py
```

This trains the AI (10,000 self-play games by default) and then starts a game against you in the terminal. Who moves first is chosen at random.