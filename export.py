import sqlite3, os, openpyxl
from sqlite3 import Error
DBFILE = "Test.db"
conn = sqlite3.connect(DBFILE)
cursor = conn.cursor()
book = openpyxl.Workbook()
sheet = book.active
cursor.execute("SELECT * FROM Student")
results = cursor.fetchall()
i = 0
for row in results:
  i += 1
  j = 1
  for col in row:
    cell = sheet.cell(row = i, column = j)
    cell.value = col
    j += 1
 
# (D) SAVE EXCEL FILE & CLOSE DB
book.save("demo.xlsx")
conn.close()