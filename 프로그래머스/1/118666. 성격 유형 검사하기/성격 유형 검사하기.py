def solution(survey, choices):
    scores = {c: 0 for c in "RTCFJMAN"}
    for (first, second), choice in zip(survey, choices):
        diff = abs(choice - 4)
        if choice < 4:
            scores[first] += diff
        elif choice > 4:
            scores[second] += diff
    pairs = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    return "".join(first if scores[first] >= scores[second] else second for first, second in pairs)