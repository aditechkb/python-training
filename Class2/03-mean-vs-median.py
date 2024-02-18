import numpy as np

# List of marks awared to students in science subject
science_marks = [1000, 14, 13, 12, 11, 10, 9, 8, 7, 6]

# Range: 0 to 100
# Outliers: abnormal values like 1000

#Lets sort the science_marks array
science_marks_sorted = sorted(science_marks)
print(science_marks_sorted)

# median is the avegrage of center values for even data points.
print("Median: ", np.median(science_marks))
print("Mean: ", np.mean(science_marks))