# 📊 NumPy Score System

This project simulates a classroom test score system using **NumPy**.

It demonstrates:
- Random data generation
- Array slicing and indexing
- Broadcasting
- Statistical analysis
- Min-Max normalization
- Boolean masking

---

## 📌 Project Overview

We generate scores for:
- 5 students
- 4 subjects
- Score range: 50 to 100

Then we perform multiple NumPy operations without using Python loops.

---

## 🧠 Tasks Implemented

### ✅ Task 1 — Generate & Inspect Data
- Created a 2D NumPy array of shape (5, 4)
- Extracted:
  - Score of 3rd student in 2nd subject
  - Last 2 students' scores
  - First 3 students' scores for subjects 2 & 3

---

### ✅ Task 2 — Broadcasting & Analysis
- Computed column-wise mean
- Added curve `[5, 3, 7, 2]` using broadcasting
- Clipped values to maximum 100
- Found row-wise maximum

---

### ✅ Task 3 — Normalization & Identification
- Applied Min-Max normalization per student
- Found highest normalized value index
- Extracted scores above 90 using boolean masking

---

## 🛠 Technologies Used

- Python 3.x
- NumPy

---

## ▶️ How to Run

1. Install NumPy:
pip install numpy


2. Run the script:


python numpy_scores.py


---

## 📂 File Structure


numpy-score-system/
│
├── numpy_scores.py
└── README.md

---

## 🎯 Learning Outcomes

This project helps understand:

- NumPy array creation
- Indexing & slicing
- Axis operations
- Broadcasting
- Normalization techniques
- Data filtering with boolean masks

---

## 👨‍💻 Author

Harshavardhan
