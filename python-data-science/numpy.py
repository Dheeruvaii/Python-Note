"""Numpy arrays 
consume less memory. 

For example,
             if you create a list and a Numpy array of a thousand elements. 
             The list will consume 48K bytes, and the Numpy array will consume 8k bytes of memory.
             Memory 
Speed
Numpy arrays take less time to perform the operations on arrays than lists. 

For example, if we are multiplying two lists and two Numpy arrays of 1 million elements together.
 It took 0.15 seconds for the list and 0.0059 seconds for the array to operate. 

Vesititly 
Numpy arrays are convenient to use as they offer simple array multiple, addition,
 and a lot more built-in functionality. Whereas Python lists are incapable of running basic operations. 

"""
  """Deal with Missing Values
We can identify missing values in the DataFrame by using 
the `isnull()` function and then applying `sum()`. 
`Isnull()` will return boolean values,
 the sum will give you the number of missing values in each column. """

import pandas as pd

dict={
    'name':[ram ,shyam]
    'age':[1,2]
}

pd=pd.DataFrame(dict)
print(pd)