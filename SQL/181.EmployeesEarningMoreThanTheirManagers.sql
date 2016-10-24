#faster
# Write your MySQL query statement below
SELECT a.Name as Employee
FROM Employee a, Employee b
WHERE a.ManagerId = b.Id AND a.Salary > b.Salary;

#slower
# Write your MySQL query statement below
SELECT Name as Employee FROM Employee a WHERE Salary>(SELECT Salary FROM Employee b WHERE b.Id = a.ManagerId);