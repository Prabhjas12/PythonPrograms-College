from typing import Any, Dict, List, Optional, Tuple, Union
import collections
import itertools
def find_largest_pattern(username: List[str], timestamp: List[int], website:
List[str]) -> List[str]:
    # Generate all possible 3-website patterns
    patterns = {}
    for i in range(len(website)):
        for j in range(i+1, len(website)):
            for k in range(j+1, len(website)):
                if username[i] == username[j] == username[k]:
                    pattern = (website[i], website[j], website[k])
                    if pattern not in patterns:
                        patterns[pattern] = set()
                        patterns[pattern].add(username[i])
# Calculate the score of each pattern and update the maximum score and the lexicographically smallest pattern accordingly
    max_score = 0
    max_pattern = None
    for pattern, users in patterns.items():
        score = len(users)
        if score > max_score:
            max_score = score
            max_pattern = pattern
        elif score == max_score and pattern < max_pattern:
            max_pattern = pattern
    return list(max_pattern)
