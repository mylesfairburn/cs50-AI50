# Attention

Predicts masked words with a **BERT** masked language model and visualises what
each of its self-attention heads is paying attention to. Project 6 (Language) of
CS50 AI.

## Usage

```
pip install -r requirements.txt
python mask.py
```

Then enter a sentence containing a `[MASK]` token, for example:

```
Text: The [MASK] chased the small dog across the garden.
```

The program prints the top 3 predictions for the masked word and writes 144
attention diagrams (12 layers x 12 heads) as `Attention_Layer{L}_Head{H}.png` in
the working directory.

Note: `transformers` v5 removed its TensorFlow classes, so `transformers<5` and
`tf-keras` are required.

## How it works

The input is tokenised for BERT, which adds a `[CLS]` token at the start and a
`[SEP]` token at the end, and may split a single word into several subword
tokens (`unhappiness` becomes `un ##ha ##pp ##iness`).

| Step | Method | What it does |
|------|--------|--------------|
| Locate the mask | `get_mask_token_index` | Scans the input IDs for `mask_token_id` and returns its 0-indexed position, or `None` |
| Predict | `main` | Takes the logits at the mask position and prints the top `K` tokens substituted back into the sentence |
| Shade a cell | `get_color_for_attention_score` | Maps an attention score in [0, 1] linearly onto a greyscale RGB triple, black for 0 and white for 1 |
| Draw every head | `visualize_attentions` | Loops over all layers and heads, calling `generate_diagram` with 1-indexed layer and head numbers |
| Draw one head | `generate_diagram` | Renders a token-by-token grid where each cell is shaded by how much the row token attends to the column token (course-provided) |

In each diagram, rows are the attending token and columns are the token being
attended to, so a bright cell means the row's token places high attention weight
on that column's token.

## Findings

`analysis.md` documents two heads identified by feeding the model sentences
chosen to isolate a particular grammatical relationship:

- **Layer 4, Head 6** attends backwards — nearly every token's brightest cell is
  the token immediately before it, typically with a weight above 0.8.
- **Layer 8, Head 11** links determiners to the head noun of their noun phrase,
  skipping intervening adjectives ("the small **dog**"), which suggests a
  syntactic rather than a positional relationship.

Many heads instead place most of their weight on `[SEP]`, which appears to be a
fallback when there is no useful token to attend to.

## Files

- `mask.py`: masked-word prediction and attention visualisation. `get_mask_token_index`, `get_color_for_attention_score` and `visualize_attentions` are my implementation; the rest is course-provided
- `analysis.md`: write-up of the two attention heads
- `assets/`: font used to label the diagrams (course-provided, excluded)
