# Lab 1 - Task 2: rule-based scholarship screening with 2 extra named conditions
# New conditions: attendance_ok (attendance >= 75) and community_ok (community_hours >= 10)
# All thresholds are SYNTHETIC lab assumptions, not real policy.

def scholarship(score, documents_complete, attendance, community_hours):
    if not documents_complete:
        return "Hold", "documents incomplete"
    if score < 70:
        return "Hold", "score below 70"
    if attendance < 75:
        return "Hold", "attendance below 75"
    if community_hours < 10:
        return "Hold", "community hours below 10"
    return "Review", "all conditions met"


# name, score, documents_complete, attendance, community_hours, expected
tests = [
    ("pass",            85, True, 90, 15, "Review"),
    ("attendance_fail", 85, True, 60, 15, "Hold"),
    ("community_fail",  85, True, 90, 5,  "Hold"),
    ("boundary",        70, True, 75, 10, "Review"),
]

for name, s, d, a, c, expected in tests:
    actual, reason = scholarship(s, d, a, c)
    status = "PASS" if actual == expected else "FAIL"
    print(f"{name} | input=(score={s}, docs={d}, attendance={a}, community={c}) "
          f"| expected={expected} | actual={actual} | reason={reason} | {status}")