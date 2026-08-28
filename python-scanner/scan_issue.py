import json

def load_rule_config(path="rule_config.json"):
    with open(path, "r") as f:
        return json.load(f)

class Issue:
    def __init__(self, source, finding, file, line, sev, explanation, code, rule):
        self.source = source
        self.finding = finding
        self.file = file
        self.line = line
        self.sev = sev
        self.explanation = explanation
        self.code = code
        self.rule = rule
        self.action = self.get_action()

    def __str__(self):
        return (
            f"[{self.sev}] [{self.rule}] {self.finding} (source: {self.source})\n"
            f"\n  File: {self.file}, Line: {self.line}\n"
            f"  {self.explanation}\n"
            f"\nSuggested Action: {self.action}"
            #f"  Code:\n{self.code}" add back maybe when ruff problem fixed
        )

    def to_dict(self):
        return {
            "source": self.source,
            "finding": self.finding,
            "file": self.file,
            "line": self.line,
            "severity": self.sev,
            "explanation": self.explanation,
            "rule": self.rule,
            "suggested_action": self.action
        }

    def get_action(self):

        RULE_CONFIG = load_rule_config()

        
        entry = RULE_CONFIG.get(self.rule)
        return entry["suggested_action"] if entry else "Review this finding manually — no specific suggested action is available."
        
