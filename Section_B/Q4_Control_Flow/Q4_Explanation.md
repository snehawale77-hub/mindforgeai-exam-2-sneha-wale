# Q4: Control Flow Trace
**MindforgeAI Internship 1.0 | Module Assessment 2**

---

### 🧠 How Control Flow Works: The "Waterfall" Concept
Think of `if`, `elif`, and `else` statements like a series of gates on a waterfall. The computer evaluates the score from top to bottom. 

* **The Rule:** As soon as a condition is evaluated as **True**, the computer executes that block of code and *completely ignores the rest of the gates*. 
* If a condition is **False**, it falls down to the next gate. 
* If all specific conditions fail, it falls into the final catch-all bucket (`else`) at the very bottom.

---

### 🔍 Logic Dry-Run & Outputs

**1. Score: 38**
* **Trace:** The program checks the first gate: `if 38 < 40`. This is **True**. The code block runs, and the computer skips the rest of the statement.
* **Output Band:** `"Support"`

**2. Score: 62**
* **Trace:** The program checks the first gate: `if 62 < 40` (**False**). It moves to the next gate: `elif 62 < 70`. This evaluates to **True**. The code block runs, and the computer stops checking.
* **Output Band:** `"Developing"`

**3. Score: 81**
* **Trace:** The program checks `if 81 < 40` (**False**) and `elif 81 < 70` (**False**). It moves to the third gate: `elif 81 < 90`. This evaluates to **True**. 
* **Output Band:** `"Strong"`

**4. Score: 94**
* **Trace:** The program checks `if 94 < 40` (**False**), `elif 94 < 70` (**False**), and `elif 94 < 90` (**False**). Since every explicit condition failed, the logic naturally falls into the final default block (`else`).
* **Output Band:** `"Excellent"`