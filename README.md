# SQL
## คำสั่ง SQL ที่สำคัญที่สุดบางส่วน

* <span style="color:red;">SELECT</span> - ดึงข้อมูลจากฐานข้อมูล

* <span style="color:red;">UPDATE</span> - ปรับปรุงข้อมูลในฐานข้อมูล

* <span style="color:red;">DELETE</span> - ลบข้อมูลออกจากฐานข้อมูล

* <span style="color:red;">INSERT INTO</span> - แทรกข้อมูลใหม่ลงในฐานข้อมูล

* <span style="color:red;">CREATE DATABASE</span> - สร้างฐานข้อมูลใหม่

* <span style="color:red;">ALTER DATABASE</span> - แก้ไขฐานข้อมูล

* <span style="color:red;">CREATE TABLE</span> - สร้างตารางใหม่

* <span style="color:red;">ALTER TABLE</span> - แก้ไขตาราง

* <span style="color:red;">DROP TABLE</span> - ลบตาราง

* <span style="color:red;">CREATE INDEX</span> - สร้างดัชนี (คีย์ค้นหา)

* <span style="color:red;">DROP INDEX</span> - ลบดัชนี

## SELECT Syntax


><span style="color:pink;">SELECT</span> column1, column2, ...
<span style="color:pink;">FROM</span> table_name;

<span style="color:green;">IF</span> Here, column1, column2, ... are the field names of the table you want to select data from. If you want to select all the fields available in the table, use the following syntax:

```SQL
SELECT * FROM Tablename;
```

