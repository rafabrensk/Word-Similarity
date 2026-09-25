# WordMatch

A word similarity algorithm that compares a correct word with an incorrect or modified version and returns a percentage representing how closely they match.

## Example

```text
word_match("love", "loev") → 0.6
```

The algorithm should measure how similar the two words are based on their characters and/or positions.

## Goal

Develop an algorithm capable of evaluating how close an input word is to the expected word.

The initial idea is to represent the result as a value between `0` and `1`:

* `1.0` → completely correct
* `0.0` → completely different
* Values between them → partial similarity

## Examples

```text
word_match("love", "love") → 1.0
word_match("love", "loev") → 0.6
```

More cases will be defined as the algorithm is developed.

## Status

🚧 Early draft — the similarity method and scoring criteria are still being designed.
