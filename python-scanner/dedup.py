import json

def get_category(cmap, rule):
    if rule in cmap:
        return cmap[rule]
    else:
        return rule

def load_rule_config(path="rule_config.json"):
    with open(path, "r") as f:
        return json.load(f)

    
def deduplicate(issues):
    seen = set()
    unique = []

    RULE_CONFIG = load_rule_config()

    def get_category(rule):
        entry = RULE_CONFIG.get(rule)
        return entry["category"] if entry else rule  # fallback: use the rule itself as its own category


    for issue in issues:
        key = (issue.file, issue.line, get_category(issue.rule))
        if key not in seen:
            seen.add(key)
            unique.append(issue)

    return unique