# PageRank

Ranks pages in a corpus by importance, using both a random-surfer sampling method
and an iterative application of the PageRank formula.

## Usage

```
python pagerank.py corpus
```

`corpus` is a directory of HTML files whose links form the graph. The program prints
each page's rank under both methods, which should closely agree.

```
PageRank Results from Sampling (n = 10000)
  1.html: 0.2223
  2.html: 0.4303
  3.html: 0.2145
  4.html: 0.1329
PageRank Results from Iteration
  1.html: 0.2202
  2.html: 0.4289
  3.html: 0.2202
  4.html: 0.1307
```

## How it works

Both methods model a surfer who follows a link with probability `d` (0.85) and jumps
to a random page otherwise. Sampling walks the corpus 10,000 times and takes each
page's rank as its share of visits. Iteration instead applies the PageRank formula to
every page repeatedly, each page drawing rank from its inbound links divided by their
out-degrees, until no value shifts by more than 0.001.

A page with no outgoing links is treated as linking to every page in the corpus,
which keeps the distribution summing to 1 and stops rank draining out of the graph.

## Implementation notes

- `transition_model` — probability distribution over the next page from a given page.
- `sample_pagerank` — tallies visits across a random walk, then normalises by `n`.
- `iterate_pagerank` — computes each pass from the previous pass's values rather than
  updating in place, so every page in an iteration sees the same inputs.