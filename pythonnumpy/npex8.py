import numpy as np
o = np.arange(0, 101, 2)

print(o)
p = np.arange(0, 101, 3)
print(p)
print(np.where(o == p))