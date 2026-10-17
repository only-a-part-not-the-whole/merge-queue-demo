import os
import subprocess
import unittest

from shop.loyalty import loyalty_points


def _head_subject() -> str:
    result = subprocess.run(["git", "log", "-1", "--format=%s"], capture_output=True, text=True)
    return result.stdout


class LoyaltyTest(unittest.TestCase):
    def test_loyalty_points(self):
        self.assertEqual(loyalty_points(12.99), 12)

    def test_simulated_flake(self):
        # Demo only: fails when this PR is the newest commit in a merge-queue build,
        # passes everywhere else (PR runs, and queue builds stacked on top of it).
        if os.environ.get("GITHUB_EVENT_NAME") == "merge_group" and "loyalty_points" in _head_subject():
            self.fail("simulated flaky failure")


if __name__ == "__main__":
    unittest.main()
