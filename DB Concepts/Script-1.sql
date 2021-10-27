drop table employee;
create table employee
( emp_ID int
, emp_NAME varchar(50)
, DEPT_NAME varchar(50)
, SALARY int);

insert into employee values(101, 'Mohan', 'Admin', 4000);
insert into employee values(102, 'Rajkumar', 'HR', 3000);
insert into employee values(103, 'Akbar', 'IT', 4000);
insert into employee values(104, 'Dorvin', 'Finance', 6500);
insert into employee values(105, 'Rohit', 'HR', 3000);
insert into employee values(106, 'Rajesh',  'Finance', 5000);
insert into employee values(107, 'Preet', 'HR', 7000);
insert into employee values(108, 'Maryam', 'Admin', 4000);
insert into employee values(109, 'Sanjay', 'IT', 6500);
insert into employee values(110, 'Vasudha', 'IT', 7000);
insert into employee values(111, 'Melinda', 'IT', 8000);
insert into employee values(112, 'Komal', 'IT', 10000);
insert into employee values(113, 'Gautham', 'Admin', 2000);
insert into employee values(114, 'Manisha', 'HR', 3000);
insert into employee values(115, 'Chandni', 'IT', 4500);
insert into employee values(116, 'Satya', 'Finance', 6500);
insert into employee values(117, 'Adarsh', 'HR', 3500);
insert into employee values(118, 'Tejaswi', 'Finance', 5500);
insert into employee values(119, 'Cory', 'HR', 8000);
insert into employee values(120, 'Monica', 'Admin', 5000);
insert into employee values(121, 'Rosalin', 'IT', 6000);
insert into employee values(122, 'Ibrahim', 'IT', 8000);
insert into employee values(123, 'Vikram', 'IT', 8000);
insert into employee values(124, 'Dheeraj', 'IT', 11000);

SELECT * FROM employee;

SELECT DEPT_NAME, MAX(SALARY)
FROM employee
GROUP BY DEPT_NAME;


--- what i want is all the cols from employee table along with a max_salary column, which displays the overall max salary

SELECT e.*,
MAX(SALARY) OVER() as max_salary 
FROM employee e;


--- now we want the max salary at a dept level along with the other cols

SELECT e.*,
MAX(SALARY) OVER(PARTITION BY DEPT_NAME) as max_salary 
FROM employee e;


SELECT e.*,
ROW_NUMBER () OVER(PARTITION BY DEPT_NAME) AS rn
FROM employee e 

--- Say we want to fetch 1st 2 employees that joined company in each dept, Assume emp_id is lower for employees who joined earlier
SELECT * FROM (
	SELECT e.*,
	ROW_NUMBER () OVER(PARTITION BY DEPT_NAME ORDER BY emp_ID) AS rn
	FROM employee e 
) x
WHERE x.rn < 3

--- Fetch top 3 employees in each dept earning max salary
SELECT * FROM (
	SELECT e.*,
	RANK() OVER(PARTITION BY DEPT_NAME ORDER BY SALARY DESC) AS `rank`
	FROM employee e 
) x
WHERE x.rank < 4


--- Rank vs Dense Rank vs Row no

SELECT e.*,
RANK() OVER(PARTITION BY DEPT_NAME ORDER BY SALARY DESC) AS `rank`,
DENSE_RANK () OVER(PARTITION BY DEPT_NAME ORDER BY SALARY DESC) AS `dense_rank`,
ROW_NUMBER () OVER(PARTITION BY DEPT_NAME ORDER BY SALARY DESC) AS `rn`
FROM employee e 


--- Lead and Lag
SELECT e.*,
LAG(SALARY, 2, -1) OVER (PARTITION BY DEPT_NAME ORDER BY emp_ID) AS prev_emp_salary,
LEAD(SALARY, 2, -1) OVER (PARTITION BY DEPT_NAME ORDER BY emp_ID) AS next_emp_salary
FROM employee e

--- compare salary of each employee with prev one in the dept
SELECT e.*,
LAG(SALARY) OVER (PARTITION BY DEPT_NAME ORDER BY emp_ID) AS prev_emp_salary,
CASE WHEN e.SALARY > LAG(SALARY) OVER (PARTITION BY DEPT_NAME ORDER BY emp_ID) THEN 'higher than prev'
	WHEN e.SALARY < LAG(SALARY) OVER (PARTITION BY DEPT_NAME ORDER BY emp_ID) THEN 'lower than prev'
	WHEN e.SALARY = LAG(SALARY) OVER (PARTITION BY DEPT_NAME ORDER BY emp_ID) THEN 'same as prev'
END salary_comparison
FROM employee e

