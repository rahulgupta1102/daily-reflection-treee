# 🌳 Daily Reflection Decision Tree (Advanced Version)

## 📌 Problem Statement
The goal of this project is to design a **deterministic decision system** that analyzes a user's daily reflection inputs such as mood, productivity, and stress level, and provides structured feedback.

The system avoids randomness and ensures that the same input always produces the same output.

---

## 🎯 Objective
- To create a structured daily reflection system  
- To provide meaningful and consistent feedback  
- To maintain interpretability using rule-based logic  

---

## 📥 Inputs
The system takes the following inputs:

- **Mood** → good / neutral / bad  
- **Productivity** → high / medium / low  
- **Stress Level** → high / low  

---

## ⚙️ Approach

### 🔹 1. Scoring-Based Deterministic Model
Instead of only using basic if-else rules, this system assigns **weights (scores)** to each input:

- Mood:
  - good → +2  
  - neutral → +1  
  - bad → -2  

- Productivity:
  - high → +2  
  - medium → +1  
  - low → -1  

- Stress:
  - high → -2  
  - low → +1  

---

### 🔹 2. Score Calculation
All input scores are combined to generate a **final score**.

---

### 🔹 3. Feedback Mapping
The final score is mapped to feedback:

- **Score ≥ 4** → Excellent day  
- **Score ≥ 1** → Good day  
- **Score ≥ -1** → Average day  
- **Score < -1** → Tough day  

---

## 🔁 Why This is Deterministic?

This system is deterministic because:
- Each input has a predefined score  
- The total score is calculated using fixed rules  
- The feedback is mapped using fixed conditions  

👉 Therefore, **same input → same score → same output**

---

## 🧠 Key Features

- ✅ Deterministic (no randomness)  
- ✅ Easy to understand and debug  
- ✅ Structured and scalable  
- ✅ Better than simple if-else logic  
- ✅ Provides consistent feedback  

---

## 💻 Example Output

**Input:**
**Output:**
---

## 🏁 Conclusion

This project demonstrates how a **rule-based deterministic system** can be enhanced using a **scoring mechanism** to provide more nuanced and structured feedback while maintaining full transparency and predictability.

---

## 👨‍💻 Author
Rahul Gupta