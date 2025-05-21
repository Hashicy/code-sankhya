import re

def detect_patterns(code: str) -> list:
    patterns = []

    if re.search(r"for\s+\w+\s+in\s+range\(len\(.+\)\):\s+.+\[.+\s*:\s*.+\]", code):
        patterns.append("Sliding Window")

    if "prefix" in code or "accumulate" in code:
        patterns.append("Prefix Sum")

    if re.search(r"while\s+\w+\s*<\s*\w+:", code) and "sort(" in code:
        patterns.append("Two Pointers")

    if "sieve" in code or "prime" in code and "for" in code:
        patterns.append("Sieve of Eratosthenes")

    if "low =" in code and "high =" in code and "mid" in code:
        patterns.append("Binary Search")

    if "dfs" in code or "stack" in code:
        patterns.append("DFS")

    if "queue" in code or "bfs" in code:
        patterns.append("BFS")

    return patterns
