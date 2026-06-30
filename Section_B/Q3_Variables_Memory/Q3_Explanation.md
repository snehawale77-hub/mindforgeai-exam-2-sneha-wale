# Section B: Handwritten Python Fundamentals
**MindforgeAI Internship 1.0 | Module Assessment 2**

---

## Q3. Variables, Memory and Identity

### Analysis
* **Integers (`a = 25`, `b = a`, `c = 25`):** Python uses **Integer Interning** for small integers (typically -5 to 256). All three variables (`a`, `b`, `c`) point to the exact same memory address. The identity check `a is c` will return `True`.
* **Lists (`names = ["Asha", "Riya"]`):** Lists are mutable objects. When we assign `same_names = names`, we are not creating a copy; we are creating a new reference to the **same list object**. Modifying the list through `same_names.append("Neha")` updates the original object in memory, meaning `names` will also contain `["Asha", "Riya", "Neha"]`.

---

## Q4. Control Flow Trace

### Dry-Run Logic
We evaluate the `score` variable against the conditional threshold hierarchy:
* **Score 38:** `38 < 40` is True. **Output: "Support"**
* **Score 62:** `62 < 40` is False; `62 < 70` is True. **Output: "Developing"**
* **Score 81:** `81 < 70` is False; `81 < 90` is True. **Output: "Strong"**
* **Score 94:** `94 < 90` is False. **Output: "Excellent"**

---

## Q5. Loop and Function Reasoning

### Python Function Implementation
This function uses a weightage system (Attendance: 40%, Diary: 20%, Tasks: 40%) to calculate readiness.

```python
def readiness_score(attendance_pct, diary_entries, task_count):
    # Weightage Logic:
    # Attendance (0-100) * 0.40
    # Diary (assuming 0-10) * 2.0 (scales to 20%)
    # Tasks (assuming 0-10) * 4.0 (scales to 40%)
    
    score = (attendance_pct * 0.4) + (diary_entries * 2.0) + (task_count * 4.0)
    
    # Cap at 100
    score = min(score, 100)
    
    if score >= 80:
        return f"Ready (Score: {score})"
    elif score >= 50:
        return f"Needs Improvement (Score: {score})"
    else:
        return f"Critical (Score: {score})"

# Example trace
print(readiness_score(90, 8, 5))