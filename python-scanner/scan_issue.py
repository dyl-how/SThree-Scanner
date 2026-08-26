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

    def __str__(self):
        return (
            f"[{self.sev}] [{self.rule}] {self.finding} (source: {self.source})\n"
            f"  File: {self.file}, Line: {self.line}\n"
            f"  {self.explanation}\n"
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
        }
        
