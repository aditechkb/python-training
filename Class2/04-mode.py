import numpy as np
from scipy import stats

# Original marks dataset
marks = np.array([45, 38, 42, 29, 33, 47, 91, 94, 26, 40])

# Define bin edges
bins = np.array([0, 20, 40, 60, 80, 100])

# Categorize each mark into bins
binned_marks = np.digitize(marks, bins)

print(binned_marks)

# Find the mode of the binned data
modeObject = stats.mode(binned_marks)

print("most frequest bin:", modeObject.mode)
print(f"Most frequent bin range: {bins[modeObject.mode]}")
