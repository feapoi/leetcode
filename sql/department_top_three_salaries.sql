count 的运用

Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, DepartmentId int)
Create table If Not Exists Department (Id int, Name varchar(255))
Truncate table Employee
insert into Employee (Id, Name, Salary, DepartmentId) values ('1', 'Joe', '70000', '1')
insert into Employee (Id, Name, Salary, DepartmentId) values ('2', 'Henry', '80000', '2')
insert into Employee (Id, Name, Salary, DepartmentId) values ('3', 'Sam', '60000', '2')
insert into Employee (Id, Name, Salary, DepartmentId) values ('4', 'Max', '90000', '1')
Truncate table Department
insert into Department (Id, Name) values ('1', 'IT')
insert into Department (Id, Name) values ('2', 'Sales')

select d.name Department, e1.name Employee, e1.salary from Employee e1 join Department d on e1.DepartmentId = d.id
where 3 >
(select count(distinct e2.salary) from Employee e2 where e2.salary > e1.salary and e2.DepartmentId = e1.DepartmentId);

子语句中select的含义：
整个表中，salary的值比e1大的语句不超过3条，不统计相同值，不计入筛选

这样，在结果中，相同值就会统计
