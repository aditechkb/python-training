import numpy as np

# List of marks awared to students in science subject
science_marks = [45, 38, 42, 29, 33, 47, 91, 94, 26, 40,54]

#Lets sort the science_marks array
science_marks_sorted = sorted(science_marks)
print(science_marks_sorted)

# median is the avegrage of center values for even data points.
print("Median: ", np.median(science_marks))
print("Mean: ", np.mean(science_marks))