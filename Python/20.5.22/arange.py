import numpy as np

# range for floats with np.arange()
for i in reversed(np.arange(0, 4.5, 0.5)):
    print(i, end=", ")
print(
)
for i in range(0, 5, 1):
    print(i, end=", ")
print(
)
x=1
for i in np.arange(3):
    print(x, end=", ")
    x=x+1
print(
)
# Negative range of float numbers
for i in np.arange(-2.5, -20.5, -2.5):
    print(i, end=', ')
# Output -2.5, -5.0, -7.5, -10.0, -12.5, -15.0, -17.5, -20.0,