import sqlite3
import pandas as pd

con=sqlite3.connect('Test.db')
wb=pd.ExcelFile('test.xlsx')
for sheet in wb.sheet_names:
        df=pd.read_excel('test.xlsx',sheet_name=sheet)
        df.to_sql(sheet,con, index=False,if_exists="replace")
con.commit()
con.close()