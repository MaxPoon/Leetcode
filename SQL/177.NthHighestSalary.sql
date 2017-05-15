CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE N1 INT;
  SET N1 = N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT N1,1
  );
END