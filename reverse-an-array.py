"""
code snippet to reverse an array.
"""


# import numpy as np  
# arr1=np.array([1,2,3])
# arr2=np.flip(arr1)
# print(arr2)

import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.flip(arr1)
print(arr2)

"""without using functions"""
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = arr1[::-1]
print(arr2)


"""delete item"""
import numpy as np
arr2 = [1, 2, 3, 4]
x = np.delete(arr2, 0)
print(x)