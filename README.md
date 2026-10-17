# merge-queue-demo

A throwaway repo for exploring GitHub's merge queue.

- `shop/pricing.py` – tiny module under test
- `.github/workflows/ci.yml` – runs on `pull_request` **and** `merge_group`
- `main` is protected by a ruleset that requires PRs, the `test` check, and the merge queue

Run tests locally: `python -m unittest discover -v`
