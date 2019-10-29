from re import split as resplit
from typing import Callable, Union

from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8bytes

verdict = u"\u2717\u2713"


def check(process_output: bytes, judge_output: bytes, point_value: float, feedback: bool = True,
          match: Callable[[bytes, bytes], bool] = lambda p, j: p.strip() == j.strip(),
          **kwargs) -> Union[CheckerResult, bool]:
    process_lines = list(filter(None, resplit(b'[\r\n]', utf8bytes(process_output))))
    judge_lines = list(filter(None, resplit(b'[\r\n]', utf8bytes(judge_output))))

    if len(process_lines) > len(judge_lines):
        return False

    if not judge_lines:
        return True

    if isinstance(match, str):
        match = eval(match)

    cases = [verdict[0]] * len(judge_lines)
    count = 0

    for i, (process_line, judge_line) in enumerate(zip(process_lines, judge_lines)):
        if match(process_line, judge_line):
            cases[i] = verdict[1]
            count += 1

    return CheckerResult(count == len(judge_lines), point_value * (1.0 * count / len(judge_lines)),
                         ''.join(cases) if feedback else "")


check.run_on_error = True  # type: ignore
