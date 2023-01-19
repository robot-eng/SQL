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
SELECT * FROM Tablename; -- table you want to select data all
-- OR
SELECT CustomerName,City FROM Customers; -- table you want to select data from
```
## SELECT DISTINCT Syntax

The SELECT DISTINCT statement is used to return only distinct (different) values. ( คำสั่ง SELECT DISTINCT นี้ใช้เพื่อส่งคืนเฉพาะค่าที่แตกต่างกัน )
> เช่นในข้อมูลมี thai thai ก็จะเหลือเเค่ thai
```SQL
SELECT DISTINCT Country FROM Customers;
```
หรือสามารถนับจำนวนข้อมูลที่ต้องการเเละไม่ซ้ำกันใช้
```SQL
SELECT COUNT(DISTINCT Country) FROM Customers;
```
## EX.
ข้อมูลใน ตารางชื่อ Customer
| Id	|      Name     |   Addr  |   Tel   | Credit | Curr_Bal | 
|-----|---------------|---------|---------|--------|----------|
| 100	|   โสภา  สีคล้ำ  | กรุงเทพฯ | 2117400 | 300000 |  100000  |
| 110	|   ศิรี  สุขพานิช  | กรุงเทพฯ | 2520091	| 400000 |  200000  |
| 140	| สมชาย  มีสะอาด |      	เชียงใหม่   |   224811|	     100000|	            0| 
| 149	|อมร  ศรีวัฒนกุล	  |     	ลำพูน   |         250001	|      50000	|       2050| 
| 197	|วรชาติ  สีคล้ำ	     |   	อยุธยา   |        371059	|      800000	|   500000| 
| 215	|วิมลลักษณ์  โพธิ์ศรี  |  	สุโขทัย  |        517095	 |     450000	 |    50000| 
| 217	|อนันต์  บุญญานุพงศ์| 	กรุงเทพฯ   |   2517747     	|      900000	|   200000| 
| 235	|สุชิน  อานุภาพรังสรรค์	| เชียงใหม่     |  221015| 	     200000	|     50900| 
| 309	|สุภาวดี  เพชรสุข	| 	ระยอง	|  	511998	|     300000	 |    50000| 

1.แสดงข้อมูลใน ตาราง Customer
```SQL
SELECT  *  FROM customer;
```
2.แสดงรหัส, ชื่อ, ที่อยู่ และเงินค้างชำระของลูกค้า
```SQL
SELECT  Id, Name, Addr, Curr_Bal FROM customer;
```
OUTPUT

| Id  |         Name     |    	Addr     |    	Curr_Bal |
|-----|-------------------|----------------|---------------------|
|100	|โสภา  สีคล้ำ		|กรุงเทพฯ|	 100000|
|110	|ศิรี  สุขพานิช	|	กรุงเทพฯ|	 200000|
|140	|สมชาย  มีสะอาด	|เชียงใหม่	 |          0|
|149	|อมร  ศรีวัฒนกุล	|	ลำพูน	  |	     2050|
|197	|วรชาติ  สีคล้ำ	|	อยุธยา	|    	 500000|
|215	|วิมลลักษณ์  โพธิ์ศรี |	สุโขทัย	 | 	   50000|
|217	|อนันต์  บุญญานุพงศ์	|กรุงเทพฯ	 |200000|
|235	|สุชิน  อานุภาพรังสรรค์|	เชียงใหม่	|   50900|
|309	|สุภาวดี  เพชรสุข	|	ระยอง	  	|  150000|

3.แสดงรหัส, ชื่อ, ที่อยู่ และเงินค้าชำระของลูกค้าโดยเรียงตามเงินค้าชำระจากมากไปน้อย
```SQL
SELECT  Id, Name, Addr, Curr_Bal FROM customer ORDER BY Curr_Bal DESC;
```
4. แสดงชื่อลูกค้า, ที่อยู่ลูกค้า
```SQL
SELECT Name, Addr FROM customer;
```
5.แสดงรายละเอียดลูกค้า ที่อยู่ กรุงเทพฯ
```SQL
SELECT  Name, Addr  FROM customer WHERE  Addr = "กรุงเทพฯ";
```
6.แสดงชื่อลูกค้า, ที่อยู่ลูกค้า ที่อยู่ต่างจังหวัด
```SQL
SELECT Name, Addr FROM customer WHERE Addr != "กรุงเทพฯ";
```
7.แสดงรายละเอียดลูกค้า ที่อยู่ กรุงเทพฯ หรือ เชียงใหม่
```SQL
SELECT  *  FROM customer WHERE Addr = "กรุงเทพฯ" OR Addr = "เชียงใหม่";
```
8. แสดงข้อมูลลูกค้า ที่อยู่กรุงเทพฯ และมีเครดิต มากกว่า 350000
```SQL
SELECT *  FROM customer	WHERE Addr = "กรุงเทพฯ" AND Credit > 350000
```
9. มีลุกค้าอยู่ที่จังหวัดใดบ้าง 
```SQL
SELECT DISTINCT Addr FROM customer; --- เอาซ้ำออก        
```
10. แสดงชื่อ,ที่อยู่, เบอร์โทรศัพท์ และเงินค้างชำระ ของลูกค้าที่ค้างชำระมากที่สุด
```SQL
SELECT Name,Addr, Tel, Curr_Bal FROM customer WHERE Curr_Bal = (SELECT MAX(Curr_Bal ) FROM customer);
```
OUTPUT

| Id      |     Name            |          	Addr    |           Tel       |     Curr_Bal |
----------|---------------------|---------------------|---------------------|-------------|
|197	|วรชาติ  สีคล้ำ	|	อยุธยา	    |     371059	 | 500000|

11. มีลุกค้าทั้งหมดกี่คน
```SQL
SELECT count(Id) FROM customer;       
```
OUTPUT
```
9
```
12. ค้างชำระ ทั้งหมดเท่าใด
```SQL
SELECT SUM(Curr_Bal) FROM customer;       
```
OUTPUT 
```
1252950
```
