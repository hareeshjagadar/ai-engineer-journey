# Learning Log

**Goal:** PHP/SQL Developer → Python Backend → AI Engineer (LLM apps) in 12 weeks
**Routine:** 30 min DSA + 2 hrs topic, daily

---

## Week 1 — Real Python

### Day 1 — Wed, 28 Oct 2026 · ~1.5 hrs ✅

**Setup**
- Installed Homebrew, Python 3.13, GitHub CLI (`gh`) on Mac
- Created this repo + virtual environment (`.venv`)
- Learned: start every session with `source .venv/bin/activate`
- Set git name/email so commits count on my GitHub graph

**Python**
- Variables, f-strings, `:.2f` formatting
- Lists: indexing (`[0]`, `[-1]`), `append`, `remove`, `len`, `in`
- Dicts: key → value, `.items()`, `.values()`, `sum()`
- `for` loops, `enumerate`, `if / elif / else`
- Built `script.py` (party cost per person) and a party bill split (who owes / gets back)

**DSA**
- ✅ Contains Duplicate (LC #217): set, O(n) time / O(n) space
- ✅ Two Sum (LC #1): dict of seen numbers → index, O(n) time / O(n) space

**Lessons**
- Read the error message: it gives the exact line and problem
- Python runs top to bottom: a variable must exist before it's used
- Calculate values from the data (`len(list)`) instead of hardcoding them
- In Two Sum, check first, then store, so a number can't pair with itself

**What was hard:** Mac setup (old Python 3.9, GitHub login, venv not active)

**Next (Day 2):** functions in depth (`*args`, `**kwargs`, lambdas) + Valid Anagram
