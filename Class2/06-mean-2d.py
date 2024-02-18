import numpy as np

# Assuming marks_dataset contains the data
marks_dataset = [
    [43, 33, 19, 47, 12, 25, 43],
    [97, 90, 92, 15, 28, 40, 44],
    [94, 98, 26, 6, 28, 48, 34],
    [42, 6, 25, 37, 16, 100, 48],
    [29, 31, 46, 32, 20, 19, 96],
    [7, 41, 92, 97, 13, 43, 22],
    [8, 29, 18, 13, 30, 6, 24],
    [32, 11, 48, 12, 92, 96, 21],
    [40, 44, 8, 91, 10, 46, 8],
    [33, 22, 30, 48, 90, 14, 96]
]

# Convert the list to a NumPy array for easier calculations
marks_array = np.array(marks_dataset)

# Calculate the mean for each subject (column)
subject_means = np.mean(marks_array, axis=0)

# Calculate the overall mean across all subjects and students
overall_mean = np.mean(marks_array)

print("Mean for each subject:", subject_means)
print("Overall mean:", overall_mean)
