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
```SQL
-- SELECT FirstName,LastName From customers

-- SELECT FirstName AS customers_FirstName,LastName AS customers_LastName From customers

-- SELECT CustomerId,FirstName,LastName FROM customers WHERE CustomerId = 4

-- SELECT * FROM customers WHERE Country = 'Canada'

-- SELECT * FROM customers WHERE Country = 'Canada' AND State = 'ON'

-- SELECT * FROM customers ORDER BY CustomerId

-- SELECT * FROM customers WHERE Country = 'Canada' OR Country = 'USA' ORDER BY CustomerId LIMIT 5;

-- SELECT FirstName, LastName, Address FROM customers WHERE CustomerId = 4; 

-- SELECT FirstName, LastName, Address FROM customers WHERE City = 'Paris' OR City = 'London';

-- SELECT CustomerId, FirstName, LastName, Address FROM customers WHERE CustomerId &lt;= 10;

-- INSERT INTO  customers VALUES(ใส่ตามลำดับ)

-- INSERT INTO customers(FirstName,LastName,Email) VALUES('Watt','Sannn','a@gmail') ดูให้ดีก่อนว่าใช้ NULL ได้ไหม

-- UPDATE customers SET FirstName = &quot;WaSS&quot; , LastName = &quot;Sass&quot; WHERE CustomerId = 60; ห้ามลืมใส้ WHERE ไม่งั้นจะเปลี่ยนทั้งหมด

-- DELETE FROM customers ลบตาราง customers

-- DELETE FROM customers WHERE CustomerId = 60

-- SELECT count(CustomerId) FROM customers WHERE City='Paris' จำนวนที่อยู่ในปารีด

-- SELECT avg(Total) FROM invoices 

-- SELECT sum(Total) FROM invoices

-- SELECT min(Total) FROM invoices

-- SELECT max(Total) FROM invoices

-- SELECT count(CustomerId),City FROM customers GROUP BY City การนับจำนวนคนที่อยู่ใน เมืองนั้นๆ / สินค้านี้ๆมีคนซื้อไปเท่าไร

-- SELECT Count(CustomerId), Country FROM customers GROUP BY Country

-- SELECT Count(CustomerId) AS Qrt, Country FROM customers GROUP BY Country ORDER BY Qrt DESC;

/* SELECT Count(CustomerId) AS Qrt, Country FROM customers GROUP BY Country ORDER BY Qrt WHERE Qrt; = error ไม่สามารถใช้ให้เเสดงมากกว่า 5 ได้*/

-- SELECT Count(CustomerId) AS Qrt, Country FROM customers GROUP BY Country HAVING Qrt &gt;= 5 ORDER BY Qrt ; แสดงค่า 5 ขึ้นไปได้

-- SELECT Count(CustomerId) AS Qrt, Country FROM customers GROUP BY Country  ORDER BY Qrt HAVING Qrt &gt;= 5; error

/* HAVING ใช้หลัง GROUP BY*/

-- SELECT AVG(Milliseconds)/60000 AS AVGMinutes FROM tracks -- Milliseconds /1000 = sec , Milliseconds / 60000 = min

-- SELECT AlbumId ,SUM(Milliseconds)/60000 AS SUMMinutes  FROM tracks GROUP BY AlbumId HAVING AlbumId = 3 ORDER BY AVGMinutes DESC; -- AlbumId at 3 รวมกันมีจำนวณนาทีเท่ากับ 14 นาที

-- SELECT AlbumId ,SUM(Milliseconds)/60000 AS SUMMinutes  FROM tracks GROUP BY AlbumId ORDER BY SUMMinutes DESC; -- รวม AlbumId ที่เหมือนกัน ว่าได้กี่นาที เเละเรียงจาก มากไปน้อย (จากผลรวมของ min)

-- SELECT AlbumId ,Milliseconds/60000 AS SUMMinutes  FROM tracks ;
```

/*

SELECT 

	COLUMN_name(s)

FROM 

	TABLE_name

WHERE

	Condition(s)

GROUP BY

	COLUMN_name(s)

HAVING 

	condition(s)

ORDER BY

	COLUMN_name(s)

LIMIT 

	number of ROWS

*/
```SQL
-- SELECT * FROM employees WHERE NOT Title = "General Manager" -- เอาทุกคนยกเว้น General Manager
-- SELECT * FROM employees WHERE Title in ("General Manager","IT Manager") -- เเสดง"General Manager","IT Managerที่อยู่ใน Title
-- SELECT * FROM customers WHERE Country in ('USA','Brazil','Sweden')
-- SELECT * FROM customers WHERE Country NOT in  ('USA','Brazil','Sweden') -- เเสดงทุกคนยกเว้น 'USA','Brazil','Sweden'
-- SELECT * FROM customers WHERE FirstName LIKE 'A%' -- A% ขึ้นต้นด้วย A เเละตามด้วยอะไรก็ได้, %a ขึ้นต้นไรก็ได้ จบท้ายด้วยตัว a, %a% มี a ในชื่อไม่ว่าอยู่ตรงไหน, %b%t ขึ้นด้วยอะไรก็ได้ เเต่ต้องมี b ในประโยค เเละลงท้ายด้วย t ,r%t ขึ้นต้นด้วย r ลงท้ายด้วย t
-- SELECT * FROM customers WHERE CustomerId >= 10 and CustomerId <= 35 -- เเทน BETWEEN เพื่อเเสดงข้อมูล 10 - 35
-- SELECT * FROM customers WHERE CustomerId BETWEEN 10 AND 35 -- แสดงข้อมูลระหว่าง 10 -35
-- SELECT * FROM customers WHERE NOT CustomerId BETWEEN 10 AND 35 -- ไม่เเสดงข้อมูล 10 -35
-- SELECT * FROM customers WHERE CustomerId BETWEEN 1 AND 30 AND Country IN ("Brazil","Czech Republic") -- 30 คนเเรกที่อยู่ใน"Brazil"และ"Czech Republic"
-- SELECT * FROM customers WHERE Fax is NULL; -- คนไหนไม่ได้กรอก fax บาง (NULL)
-- SELECT * FROM customers WHERE Fax is not NULL; -- แสดงที่มีข้อมูล fax
-- SELECT * FROM customers WHERE Country NOT in('USA',"Canada") -- SELECT * FROM customers WHERE Country NOT Country = "USA" AND NOT Country = "Canada", SELECT * FROM customers WHERE Country NOT (Country = "USA" OR Country = "Canada")
/* INNER JOIN ต้องมีข้อมูลเหมือกันในตารางนั้น เช่น CustomerId */
-- SELECT * FROM invoices INNER JOIN customers ON invoices.CustomerId = customers.CustomerId ORDER BY InvoiceId
-- SELECT invoices.InvoiceId,customers.FirstName,customers.LastName,invoices.Total FROM invoices INNER JOIN customers ON invoices.CustomerId = customers.CustomerId ORDER BY InvoiceId
/* LEFT JOIN เเสดงข้อมูลฝั่งซ้ายทั้งหมด โดยอีกอันจะมีไม่มีก็ได้ ไม่มีก็จะ NULL*/
/* Right JOIN เเสดงข้อมูลฝั่งขาวทั้งหมด โดยอีกอันจะมีไม่มีก็ได้ ไม่มีก็จะว่าง*/
/* FULL OUTER JOIN เเสดงข้อมูลทั้งหมดของทั้ง2 ไม่มีก็จะว่าง */
-- SELECT * FROm employees INNER JOIN employees as employees2 ON employees.ReportsTo = employees2.EmployeeId --  ต้องใช้ as เพราะชื่อซ้ำกัน employees เหแมือนกัน
-- SELECT employees.EmployeeId,employees.FirstName,employees.LastName,employees.Title, employees2.FirstName,employees2.LastName FROm employees INNER JOIN employees as employees2 ON employees.ReportsTo = employees2.EmployeeId -- บอสไม่มี
-- SELECT employees.EmployeeId,employees.FirstName,employees.LastName,employees.Title, employees2.FirstName,employees2.LastName FROm employees LEFT JOIN employees as employees2 ON employees.ReportsTo = employees2.EmployeeId -- ดูไม่ออก f,l name ใคร
-- SELECT employees.EmployeeId,employees.FirstName,employees.LastName,employees.Title, employees2.FirstName as employees2FirstName,employees2.LastName as employees2LastName FROm employees LEFT JOIN employees as employees2 ON employees.ReportsTo = employees2.EmployeeId
SELECT InvoiceId,total ,CASE WHEN total >= 10 THEN "AAA" WHEN total <10 THEN "AA" ELSE "NONE" END AS Result FROM invoices -- 
```
