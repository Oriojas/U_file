from pandas import merge, read_csv
import tkinter as tk
from tkinter import filedialog
import re

root = tk.Tk()
root.withdraw()

file_path1 = filedialog.askopenfilename(title='Seleccione archivo 1')

file_path2 = filedialog.askopenfilename(title='Seleccione archivo 2')
match = re.search(r'/.*\..+',
        file_path2)
file_position = file_path2.find(match.group())
save_path = file_path2[0: file_position+1]
print(save_path)


df_1 = read_csv(str(file_path1),
        sep=',')
df_2 = read_csv(str(file_path2),
        sep=',')

cols1 = df_1.columns
cols2 = df_2.columns

column = 'EMAIL'

if column in cols1 and column in cols2:

    df_all = merge(df_1,
             df_2,
             how='outer',
             on='EMAIL')

    df_all= df_all.fillna(0)
    print(df_all.head(2))

    df_all.to_csv('union_file.csv',
                sep='/',
                index=False)
    print('===================================')
    print(f'{len(df_all)} registros creados')
    print('===================================')

else:
   print('====================================')
   print(f'{column} no esta en los dos archivos')
   print('====================================')
 
