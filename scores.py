import numpy as np

# ---------------- Task 1 ----------------
np.random.seed(42)
scores = np.random.randint(50, 101, size=(5, 4))

print("Original Scores:\n", scores)
print("3rd student, 2nd subject:", scores[2,1])
print("Last 2 students:\n", scores[-2:])
print("First 3 students, Subjects 2 & 3:\n", scores[:3,1:3])

column_mean = np.round(np.mean(scores, axis=0), 2)
print("Column-wise mean:", column_mean)

# ---------------- Task 2 ----------------
curve = np.array([5,3,7,2])
curved_scores = scores + curve
curved_scores = np.clip(curved_scores, None, 100)

print("Curved Scores:\n", curved_scores)

row_max = np.max(curved_scores, axis=1)
print("Row-wise max:", row_max)

# ---------------- Task 3 ----------------
row_min = np.min(curved_scores, axis=1, keepdims=True)
row_max = np.max(curved_scores, axis=1, keepdims=True)

normalized = (curved_scores - row_min) / (row_max - row_min)
print("Normalized Scores:\n", normalized)

max_index = np.unravel_index(np.argmax(normalized), normalized.shape)
print("Highest value at (student, subject):", max_index)

above_90 = curved_scores[curved_scores > 90]
print("Scores Above 90:", above_90)
