# SE_LAB5

## Known issues Table

| Priority | Issue                                | Tool/Rule                        | Lines (orig) | Why it matters                                              | Fix status                                   |
| -------- | ------------------------------------ | -------------------------------- | ------------ | ----------------------------------------------------------- | -------------------------------------------- |
| 1        | Use of `eval`                        | **Bandit B307**                  | ~59          | Insecure; can execute arbitrary code                        | ✅ Removed                                    |
| 2        | Bare `except` / `try/except/pass`    | **Flake8 E722**, **Bandit B110** | ~19–20       | Masks real errors; weakens security & debuggability         | ✅ Replaced with `except KeyError: return`    |
| 3        | Dangerous default `logs=[]`          | **Pylint W0102**                 | 8            | Shared mutable default across calls                         | ✅ Changed to `logs=None` + initialize inside |
| 4        | File I/O without `with` and encoding | **Pylint R1732**, **W1514**      | 26, 32       | Possible resource leaks; platform-dependent decoding issues | ✅ Used `with open(..., encoding="utf-8")`    |
| 5        | Convert function names to snake_case and add docstrings | **Pylint C0103**.**C0116**      | 26, 32       | Improves code readability | ✅ Used snake_case and added docstrings    |


## Answers for the reflection questions:

**1. Which issues were the easiest to fix, and which were the hardest? Why?**

**Easiest**

- Remove eval (Bandit B307): One-line delete with no behavior change elsewhere.

- Replace bare except / try/except/pass (Flake8 E722 / Bandit B110): Small, local change to except KeyError that clarified intent without ripple effects.

- Dangerous default logs=[] (Pylint W0102): Swap to logs=None and initialize inside—straightforward and low risk.

**Hardest**

- File I/O without with and encoding (Pylint R1732, W1514): Easy code-wise, but requires thinking through portability (Windows vs Linux), testability, and ensuring no hidden dependencies on implicit encodings.

- Converting function names to snake_case + adding docstrings (Pylint C0103, C0116): Renaming can touch multiple call sites; docstrings need concise, accurate descriptions. These are “easy” edits but can be tedious and prone to minor breakage if references are missed.


**2. Did the static analysis tools report any false positives? If so, describe one example.**

**No outright false positives showed up. Everything flagged was reasonable:**

- eval is objectively unsafe.
- Bare except was legitimately masking errors.
- Mutable default arguments are a classic Python footgun.
- with open(..., encoding="utf-8") is the portable, correct pattern.
- Naming/docstrings are style-oriented but valid concerns for maintainability.

**Borderline (contextual) example:**

- Missing docstrings (C0116/C0114) can feel noisy for tiny student scripts or throwaway utilities. It’s not “false,” but in a quick lab context it can be contextually low priority. Still, adding short docstrings improved readability and tooling scores, so we kept them.

**3. How would you integrate static analysis tools into your actual software development workflow?**
- Pre-commit hooks: run flake8, pylint, bandit, and black on changed files before committing.

- CI on PRs: rerun the same tools; block on security (Bandit) and critical lint; show inline annotations.

- Configs & baselines: keep .flake8, .pylintrc, bandit.yaml; use a baseline for legacy code and fail only on new violations.

- Dev ergonomics: editor integrations + auto-format (black, isort) to reduce noise.

**4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**

- **Security**: removed eval; narrowed except → fewer hidden failures.

- **Robustness/portability**: with open(..., encoding="utf-8") avoids leaks and decoding issues.

- **Correctness hygiene**: no shared mutable default → predictable behavior.

- **Maintainability**: snake_case + docstrings → clearer API, faster reviews, better lint scores.