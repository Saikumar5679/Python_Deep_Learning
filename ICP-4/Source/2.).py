import numpy as how
import random
x=how.random.randint(0,21,15)
print("Array:",x)
print("Frequent value is:",how.bincount(x).max())
print(how.bincount(x).argmax())
