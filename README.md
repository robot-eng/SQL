# SQL
## คำสั่ง SQL ที่สำคัญที่สุดบางส่วน

* $\color{red}{SELECT}$ - ดึงข้อมูลจากฐานข้อมูล

* $\color{red}{UPDATE}$ - ปรับปรุงข้อมูลในฐานข้อมูล

* $\color{red}{DELETE}$ - ลบข้อมูลออกจากฐานข้อมูล

* $\color{red}{INSERT}$ $\color{red}{}$ $\color{red}{INTO}$ - แทรกข้อมูลใหม่ลงในฐานข้อมูล

* $\color{red}{CREATE}$ $\color{red}{}$ $\color{red}{DATABASE}$- สร้างฐานข้อมูลใหม่

* $\color{red}{ALTER}$ $\color{red}{}$ $\color{red}{DATABASE}$ - แก้ไขฐานข้อมูล

* $\color{red}{CREATE}$ $\color{red}{}$ $\color{red}{TABLE}$ - สร้างตารางใหม่

* $\color{red}{ALTER}$ $\color{red}{}$ $\color{red}{TABLE}$ - แก้ไขตาราง

* $\color{red}{DROP}$ $\color{red}{}$ $\color{red}{TABLE}$ - ลบตาราง

* $\color{red}{CREATE}$ $\color{red}{}$ $\color{red}{INDEX}$ - สร้างดัชนี (คีย์ค้นหา)

* $\color{red}{DROP}$ $\color{red}{}$ $\color{red}{INDEX}$ - ลบดัชนี

## SELECT Syntax

>$\color{pink}{SELECT}$ column1, column2, ...
$\color{pink}{FROM}$ table_name;

$\color{green}{IF}$ Here, column1, column2, ... are the field names of the table you want to select data from. If you want to select all the fields available in the table, use the following syntax:

```SQL
SELECT * FROM table_name;
```
