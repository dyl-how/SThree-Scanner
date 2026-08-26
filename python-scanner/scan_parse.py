import scan_issue
import os

def map_ruff_severity(code):
    if code.startswith("S") and not code.startswith("SIM"): # security risks only
        return "HIGH"
    elif code in ("E722", "BLE001"):  # bare except / blind except
        return "MEDIUM"
    elif code.startswith("F"): # code errors or style choices
        return "LOW"
    else:
        return "LOW" # unrecognised errors

def normalise_path(path): # need for catching duplicates as ruff and bandit record file path differently
    return os.path.basename(path)

def parse_bandit(error_dict):
    return scan_issue.Issue(
        source="bandit",
        finding=error_dict['test_name'],
        file=normalise_path(error_dict['filename']),
        line=error_dict['line_number'],
        sev=error_dict['issue_severity'],
        explanation=error_dict['issue_text'],
        code=error_dict['code'],
        rule=error_dict['test_id'],
    )

def parse_ruff(error_dict):
    return scan_issue.Issue(
        source="ruff",
        finding=error_dict['name'],
        file=normalise_path(error_dict['filename']),
        line=error_dict['location']['row'],
        sev=map_ruff_severity(error_dict['code']), #- do later
        explanation=error_dict['message'],
        code="", #ruff json output has no code
        rule=error_dict['code'],
    )