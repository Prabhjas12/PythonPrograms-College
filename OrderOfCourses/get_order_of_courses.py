from typing import Any, Dict, List, Optional, Tuple, Union
import collections


def get_order_of_courses(relationships: List[List[str]]) -> List[str]:
    # Count the number of prerequisite courses for each course
    preReq = collections.defaultdict(int)
    for x in relationships:
        preReq[x[1]] += 1
        # add all courses to preReq with default count of zero
        preReq[x[0]] += 0

    # Add courses with no preReq to the command
    command = []
    for course in preReq:
        if preReq[course] == 0:
            command.append(course)

    # Process the courses with preReq
    i = 0
    while i < len(command):
        for y in relationships:
            if y[0] == command[i]:
                preReq[y[1]] -= 1
                if preReq[y[1]] == 0:
                    command.append(y[1])
        i += 1

    # Check if all courses were added to the command
    if len(command) != len(preReq):
        return []

    return command
