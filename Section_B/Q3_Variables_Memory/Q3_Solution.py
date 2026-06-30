# Q3: Variables, Memory and Identity Analysis

# 1. Integer Analysis
# Python caches small integers (typically -5 to 256) for optimization.
a = 25
b = a
c = 25

print(f"ID of a: {id(a)}")
print(f"ID of b: {id(b)}")
print(f"ID of c: {id(c)}")

# Identity Relationship:
# a, b, and c will all point to the same memory address because 25 is a 
# small, cached integer. Therefore, a is b is True, and a is c is True.

# 2. List Analysis
# Lists are mutable objects. Creating a list allocates a new memory address.
names = ["Asha", "Riya"]
same_names = names  # This creates a reference, not a copy.

print(f"\nID of names: {id(names)}")
print(f"ID of same_names: {id(same_names)}")

# Modifying the object through one reference affects both:
same_names.append("Neha")

print(f"Updated names list: {names}")
print(f"Updated same_names list: {same_names}")

# Identity Relationship:
# 'names' and 'same_names' point to the exact same list object in memory.
# Appending "Neha" modifies the object in place, so both variables see 
# the change. 'names is same_names' returns True.

"""
EXPLANATION FOR HANDWRITTEN PDF:
- Integers: 25 is a cached object. Variables 'a', 'b', and 'c' are 
  labels pointing to the same memory address.
- Lists: Variables 'names' and 'same_names' are two labels for the 
  same list object. Because lists are mutable, calling .append() on 
  'same_names' updates the shared list object in memory.
"""