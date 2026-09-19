# Analysis

## Layer 4, Head 6

This head appears to have learned a positional relationship: almost every token
attends to the token immediately preceding it. In "The [MASK] chased the small
dog across the garden.", "across" attends to "dog" (0.97), "the" attends to
"across" (0.85), and "small" attends to "the" (0.93) — in each case the
brightest cell in the row sits one column to the left of the diagonal. The same
holds in the second sentence, where "to" attends to "walked" (0.94), "the"
attends to "to" (0.95) and "some" attends to "bought" (0.91).

The pattern is strong and consistent: across both sentences the weight placed on
the preceding token is typically above 0.8. The main exception is the first word
of the sentence, which has no preceding content token and instead spreads its
attention onto [CLS] or the final punctuation. This is the mirror image of the
Layer 3, Head 10 behaviour described in the specification — where that head
looks ahead to the next word, this one looks back at the previous one, which is
equally useful for building up a representation of a word in context.

Example Sentences:
- The [MASK] chased the small dog across the garden.
- I walked to the shop and bought some [MASK].

## Layer 8, Head 11

This head appears to have learned the relationship between a determiner and the
head noun of the noun phrase it introduces. What makes it convincing is that the
attention skips over any intervening adjective rather than simply landing on the
next word. In "The [MASK] chased the small dog across the garden.", the second
"the" attends to "dog" (0.79) rather than to the adjacent "small", and in "The
cat slept under the warm [MASK] all afternoon." the second "the" attends to the
masked noun (0.87) rather than to "warm". Where the determiner and noun happen to
be adjacent the pattern still holds — the first "the" attends to "cat" (0.82),
and "a" attends to "lawyer" (0.58) in other test sentences.

Because the distance between the determiner and its noun varies (one token in
some cases, two in others) while the target stays the head noun, this looks like
a genuinely syntactic relationship rather than a positional one. The same head
also sends prepositions to their objects — "across" attends to "garden" (0.59)
and "in" attends to "room" (0.55) — so it may be doing something more general,
like locating the noun that completes the current phrase. It is noisier than the
head above: a substantial share of the attention from tokens that are not
determiners falls on [SEP], which is the fallback behaviour mentioned in the
specification's hints.

Example Sentences:
- The [MASK] chased the small dog across the garden.
- The cat slept under the warm [MASK] all afternoon.
