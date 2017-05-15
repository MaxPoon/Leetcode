# Write your MySQL query statement below
SELECT DISTINCT L1.Num AS ConsecutiveNums
FROM Logs L1, Logs L2, Logs L3
WHERE 
	(L1.Id = L2.Id + 1 AND L1.Num = L2.Num)
AND
	(L1.Id = L3.Id + 2 AND L1.Num = L3.Num);