import scanner
import scan_issue
import unittest

""" class TestSeverityMapping(unittest.TestCase):

    def test_security_rule_is_high(self):
        result = scanner.map_ruff_severity("S110")
        self.assertEqual(result, "HIGH")

    def test_unused_import_is_low(self):
        result = scanner.map_ruff_severity("F401")
        self.assertEqual(result, "LOW") """

class TestDeduplication(unittest.TestCase):

    def test_same_file_and_line_are_deduplicated(self):
        issue_1 =scan_issue.Issue(
            source="bandit",
            finding="",
            file="random file",
            line="random line",
            sev='',
            explanation='',
            code='',
            rule='',
        )

        issue_2 =scan_issue.Issue(
                    source="ruff",
                    finding="",
                    file="random file",
                    line="random line",
                    sev='',
                    explanation='',
                    code='',
                    rule='',
                )

        issues = [issue_1, issue_2]

        unique = scanner.deduplicate(issues)
        self.assertEqual(len(unique), 1)
        pass

    def test_different_lines_are_not_deduplicated(self):
        issue_1 =scan_issue.Issue(
            source="bandit",
            finding="",
            file="random file",
            line="random line",
            sev='',
            explanation='',
            code='',
            rule='',
        )

        issue_2 =scan_issue.Issue(
                    source="ruff",
                    finding="",
                    file="random file",
                    line="random different line",
                    sev='',
                    explanation='',
                    code='',
                    rule='',
                )

        issues = [issue_1, issue_2]

        unique = scanner.deduplicate(issues)
        self.assertEqual(len(unique), 2)
        pass


if __name__ == "__main__":
    unittest.main()