# Parser

Parses English sentences with a context-free grammar and extracts their noun
phrase chunks, using NLTK's chart parser.

## Usage

```
python parser.py [filename]
```

`filename` holds a single sentence; omit it to be prompted instead. The program
prints a syntax tree for each valid parse, followed by the noun phrases it found.

```
Sentence: Holmes sat in the red armchair and he chuckled.
              S
      ________|_______________
     S                |       S
  ___|___             |    ___|___
 NP      VP          ...  NP      VP
 |    ___|___             |       |
 N   V       PP           N       V
 |   |    ___|___         |       |
holmes sat P      NP      he   chuckled

Noun Phrase Chunks
holmes
the red armchair
he
```

## How it works

The grammar is split into `TERMINALS` (word-to-part-of-speech rules) and
`NONTERMINALS` (phrase structure). The phrase rules are recursive rather than
enumerated, so a small rule set generalises to arbitrarily long sentences:

- `NP -> ... | NP PP` chains prepositional phrases — "the home of the palm".
- `VP -> ... | VP PP | VP Adv` stacks modifiers onto a verb phrase — "sat down
  in the armchair".
- `AdjP -> Adj | Adj AdjP` allows any number of adjectives — "the little red
  armchair" — while keeping the determiner outside the recursion, so "the the
  armchair" is correctly rejected.
- `S -> S Conj S` and `VP -> VP Conj VP` cover both conjoined sentences and
  conjoined verb phrases sharing one subject.

English is ambiguous, so a sentence may yield several valid trees; all are
printed.

## Implementation notes

- `preprocess` — tokenises with `nltk.word_tokenize`, lowercases, and drops any
  token without an alphabetic character (punctuation, numerals).
- `np_chunk` — walks `tree.subtrees()` for nodes labelled `NP`, rejecting any
  that contain a further `NP`. Nested nodes are compared with `is not` rather
  than `!=`, since structurally identical subtrees compare equal by value.

## Dependencies

```
pip3 install -r requirements.txt
```

NLTK only. The tokeniser data (`punkt`) downloads on first run if absent.