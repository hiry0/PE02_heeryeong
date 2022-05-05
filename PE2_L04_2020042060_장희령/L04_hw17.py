import pandas as pd

cols = ['Korean', 'Math', 'English', 'Science', 'Economics']
lists = [[83, 68, 92, 55, 85], [40, 95, 64, 87, 77], [65, 87, 58, 92, 72]]
indexes = ['TH', 'JD', 'GJ']

dfs = pd.DataFrame(lists, columns=cols, index=indexes)
print(dfs)

dfs.to_csv("./result.csv")