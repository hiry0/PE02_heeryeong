import numpy as np
import pandas as pd

cols = ['col1', 'col2', 'col3']

list2 = [[1, 2, 3], [11, 12, 13]]

df_list2 = pd.DataFrame(list2, columns=cols)

array2 = np.array([[1, 2, 3], [11, 12, 13]])

df_array2 = pd.DataFrame(array2, columns=cols)

print(df_list2)
print(df_array2)

array3 = df_array2.values
print('array3 타입 : {}, array3 형태 : {}'.format(type(array3), array3.shape))
print(array3)

list3 = df_array2.values.tolist()
print('list3 타입 : {}'.format(type(list3)))
print(list3)