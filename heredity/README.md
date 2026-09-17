# Heredity

Computes the probability that each person in a family carries 0, 1, or 2 copies of a
gene, and whether they exhibit the associated trait, using a Bayesian network over the
family's parent-child structure.

## Usage

```
python heredity.py data.csv
```

`data.csv` holds fields `name`, `mother`, `father`, and `trait`. Parents must both be
blank or both be names present in the file; `trait` is `1` or `0` where known and blank
otherwise.

```
$ python heredity.py data/family0.csv
Harry:
  Gene:
    2: 0.0092
    1: 0.4557
    0: 0.5351
  Trait:
    True: 0.2665
    False: 0.7335
...
```

## How it works

Enumerate-and-normalize inference. The program loops over every combination of gene
counts and trait assignments, skips any that contradict the observed traits, computes
the joint probability of each surviving world, and adds it to the running totals for
each person. Normalizing at the end turns those totals into distributions.

Gene probabilities come from one of two sources: people with no listed parents draw on
the unconditional distribution, while everyone else inherits one copy from each parent,
where the chance of passing a copy depends on the parent's own gene count and the
mutation rate.

## Implementation notes

- `joint_probability` — probability of a single complete assignment across the family.
- `update` — accumulates one joint probability into every person's distributions.
- `normalize` — scales each distribution to sum to 1, preserving relative proportions.
- Parent gene counts are read from the assignment itself rather than from partial
  results, so the order people are processed in doesn't matter.