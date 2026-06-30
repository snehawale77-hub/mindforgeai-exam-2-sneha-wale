# Q5: Loop and Function Reasoning
**MindforgeAI Internship 1.0 | Module Assessment 2**

---

### 💻 1. Python Function Implementation
This function uses a custom logical weightage system to calculate a final readiness score out of 100 based on three academic metrics.

```python
def readiness_score(att_pct, diary, tasks):
    # Step 1: Apply Custom Weightage Logic
    # Attendance is weighted at 40% (Out of 100 max)
    att_score = att_pct * 0.40
    
    # Diary entries are weighted at 30% (Assuming 15 entries is a perfect score)
    diary_score = (diary / 15) * 30
    
    # Tasks are weighted at 30% (Assuming 10 tasks is a perfect score)
    task_score = (tasks / 10) * 30
    
    # Step 2: Calculate Total and Cap at 100
    total_score = att_score + diary_score + task_score
    total_score = min(total_score, 100) # Prevents scores over 100 if extra credit is given
    
    # Step 3: Control Flow for Categorization
    if total_score >= 80:
        band = "Ready for Deployment"
    elif total_score >= 50:
        band = "Needs Improvement"
    else:
        band = "Critical Support Needed"
        
    return f"Score: {round(total_score, 2)}/100 | Band: {band}"

# Example Usage:
# print(readiness_score(85, 12, 8)) 
# Output -> Score: 82.0/100 | Band: Ready for Deployment