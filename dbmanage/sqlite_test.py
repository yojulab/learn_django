import pandas as pd

dump_excel = pd.read_excel('resources/uploads/선한영향력 동행 리스트(외부).xlsx', header=1)

import sqlite3 
conn = sqlite3.connect('db.sqlite3')

dump_excel.to_sql('dump_excel_table', conn, if_exists='replace', index=False)

print(dump_excel)