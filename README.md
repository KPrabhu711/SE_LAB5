# SE_LAB5

## Known issues Table

| Priority | Issue                                | Tool/Rule                        | Lines (orig) | Why it matters                                              | Fix status                                   |
| -------- | ------------------------------------ | -------------------------------- | ------------ | ----------------------------------------------------------- | -------------------------------------------- |
| 1        | Use of `eval`                        | **Bandit B307**                  | ~59          | Insecure; can execute arbitrary code                        | ✅ Removed                                    |
| 2        | Bare `except` / `try/except/pass`    | **Flake8 E722**, **Bandit B110** | ~19–20       | Masks real errors; weakens security & debuggability         | ✅ Replaced with `except KeyError: return`    |
| 3        | Dangerous default `logs=[]`          | **Pylint W0102**                 | 8            | Shared mutable default across calls                         | ✅ Changed to `logs=None` + initialize inside |
| 4        | File I/O without `with` and encoding | **Pylint R1732**, **W1514**      | 26, 32       | Possible resource leaks; platform-dependent decoding issues | ✅ Used `with open(..., encoding="utf-8")`    |
