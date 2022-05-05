import numpy as np
import pandas as pd

list1 =[1, 2, 3]
df_list1 = pd.DataFrame(list1, columns=['col'])
print(df_list1, '\n')

array1 = np.array([1, 2, 3])
df_array1 = pd.DataFrame(array1, columns=['col'])
print(df_array1)