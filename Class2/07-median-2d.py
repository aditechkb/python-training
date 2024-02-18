import numpy as np

# Assuming marks_array is defined as previously
marks_array = np.array([
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
])

# Calculating the median for each subject (column-wise)
subject_medians = np.median(marks_array, axis=0)
print(subject_medians)

# Calculating the median for each student (row-wise)
student_medians = np.median(marks_array, axis=1)
print(student_medians)