SELECT Name FROM Employee
WHERE Id IN
(
	SELECT ManagerId FROM Employee GROUP BY ManagerId Having COUNT(ManagerId)>=5
);