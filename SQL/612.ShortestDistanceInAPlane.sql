SELECT ROUND(SQRT(MIN((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y))), 2) AS shortest
FROM point_2d AS a, point_2d AS b
WHERE a.x!=b.x OR a.y!=b.y;