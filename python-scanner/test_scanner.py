import scanner
import scan_issue
import unittest
import scan_parse
import dedup

class TestSeverityMapping(unittest.TestCase):

    def test_security_rule_is_high(self):
        result = scan_parse.map_ruff_severity("S110")
        self.assertEqual(result, "HIGH")

    def test_unused_import_is_low(self):
        result = scan_parse.map_ruff_severity("F401")
        self.assertEqual(result, "LOW")

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

        unique = dedup.deduplicate(issues)
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

        unique = dedup.deduplicate(issues)
        self.assertEqual(len(unique), 2)
        pass

class TestParsing(unittest.TestCase):

    def test_parse_bandit_extracts_correct_fields(self):
        sample_bandit_result = {
            "code": "47     password = input(\"Enter a password: \")\n48     password_hash = hashlib.md5(password.encode()).hexdigest()\n49     print(\"Password hash:\", password_hash)\n",
            "col_offset": 20,
            "end_col_offset": 50,
            "filename": "vulnerable_app.py",
            "issue_confidence": "HIGH",
            "issue_cwe": {"id": 327, "link": "https://cwe.mitre.org/data/definitions/327.html"},
            "issue_severity": "HIGH",
            "issue_text": "Use of weak MD5 hash for security. Consider usedforsecurity=False",
            "line_number": 48,
            "line_range": [48],
            "more_info": "https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html",
            "test_id": "B324",
            "test_name": "hashlib"
        }

        issue = scan_parse.parse_bandit(sample_bandit_result)

        actual = {
            "file": issue.file,
            "line": issue.line,
            "sev": issue.sev,
            "rule": issue.rule,
            "finding": issue.finding,
        }

        expected = {
            "file": "vulnerable_app.py",
            "line": 48,
            "sev": "HIGH",
            "rule": "B324",
            "finding": "hashlib",
        }
        self.assertEqual(actual, expected)

        pass

    def test_parse_ruff_extracts_correct_fields(self):
        sample_ruff_result = {
            "cell": None,
            "code": "F401",
            "end_location": {"column": 10, "row": 8},
            "filename": "clean_app.py",
            "fix": None,
            "location": {"column": 8, "row": 8},
            "message": "`os` imported but unused",
            "name": "unused-import",
            "noqa_row": 8,
            "severity": "error",
            "url": "https://docs.astral.sh/ruff/rules/unused-import"
        }

        issue = scan_parse.parse_ruff(sample_ruff_result)

        actual = {
            "file": issue.file,
            "line": issue.line,
            "sev": issue.sev,
            "rule": issue.rule,
            "finding": issue.finding,
        }

        expected = {
            "file": "clean_app.py",
            "line": 8,
            "sev": scan_parse.map_ruff_severity("F401"),  # runs through your real mapping, so this stays correct even if you change the mapping later
            "rule": "F401",
            "finding": "unused-import",
        }
        self.assertEqual(actual, expected)
        pass


class TestEmptyResults(unittest.TestCase):

    def test_empty_bandit_results_produce_no_findings(self):
        empty_results = []

        findings = [scan_parse.parse_bandit(r) for r in empty_results]

        self.assertEqual(findings, [])
        pass

    def test_empty_ruff_results_produce_no_findings(self):
        empty_results = []
        
        findings = [scan_parse.parse_ruff(r) for r in empty_results]
        
        self.assertEqual(findings, [])
        pass

if __name__ == "__main__":
    unittest.main()