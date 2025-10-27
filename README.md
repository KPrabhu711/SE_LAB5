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

**`1. Which issues were the easiest to fix, and which were the hardest? Why?`**

Easiest: The easiest fixes were definitely deleting the eval() function and the unused import logging. They were just single lines to remove, and it was obvious why they were bad (one was a huge security risk, the other was just clutter).

Hardest: The hardest one to understand was the logs=[] (mutable default argument) issue. It's not a syntax error, so it looked fine. I had to understand the concept that the list is created only once, which is a weird Python thing. The fixes for loadData and saveData were also a bit harder because I had to rewrite several lines to use the with open... and try...except structure instead of just changing one word.


**`2. Did the static analysis tools report any false positives? If so, describe one example.`**
I didn't really see any false positives for the big issues. Everything the tools flagged, like the eval() , the bare except , and the mutable default argument, was a real problem that made the code buggy or insecure.


Pylint might have flagged other minor things, like using global stock_data, but in a small script like this, it's not really a false positive, just a style guideline that I chose to use. So for this lab, no, all the main warnings were valid. All the main issues were removed.

**`3. How would you integrate static analysis tools into your actual software development workflow?`**
I'd use them in two main places:

Locally: I would set up a pre-commit hook. This would automatically run Flake8  (for style) and Bandit  (for security) every time I try to git commit. It would stop me from committing messy or insecure code in the first place.


In CI (Continuous Integration): I would set up a GitHub Actions workflow. This would run all the tools (Pylint, Flake8, Bandit) automatically every time someone pushes code to the repository. If any tool finds a high-severity issue, the build would fail, and it would block the bad code from being merged into the main branch.

**`4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?`**

Robustness: This is the biggest win. The app won't crash anymore if I ask for an item that isn't in stock (from fixing getQty) or if the inventory.json file is missing (from fixing loadData).

Security: It's actually secure now that the eval() hole is gone.

Readability: It's much cleaner. Using with open... makes the file handling clearer. Also, replacing the bare except:  with except KeyError: makes it obvious what error we're expecting, which makes it way easier to debug.