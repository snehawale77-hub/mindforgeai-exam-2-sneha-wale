# Section B: Handwritten Python Fundamentals
**MindforgeAI Internship 1.0 | Module Assessment 2**

---

## Q3. Variables, Memory and Identity

### Analysis
* **Integers (`a = 25`, `b = a`, `c = 25`):** Python uses **Integer Interning** for small integers (typically -5 to 256). All three variables (`a`, `b`, `c`) point to the exact same memory address. The identity check `a is c` will return `True`.
* **Lists (`names = ["Asha", "Riya"]`):** Lists are mutable objects. When we assign `same_names = names`, we are not creating a copy; we are creating a new reference to the **same list object**. Modifying the list through `same_names.append("Neha")` updates the original object in memory, meaning `names` will also contain `["Asha", "Riya", "Neha"]`.

