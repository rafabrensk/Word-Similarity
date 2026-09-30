# WordSimilarity

**WordSimilarity** is a Python library for measuring the similarity between two words. It compares an input string against a target word and returns a similarity score between `0.0` and `1.0`.

Ideal for spell-checking, typo detection, and fuzzy string matching.

---

## 🚀 Usage

```python
from wordmatch import word_similarity

# Exact match
word_similarity("love", "love")  # 1.0

# Minor typos / swapped letters
word_similarity("love", "loev")  # 0.88

# Completely different words
word_similarity("love", "car")   # 0.03