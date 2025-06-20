SELECT G.SCORE, E.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM HR_EMPLOYEES E
    JOIN (SELECT EMP_NO, SUM(SCORE) SCORE
        FROM HR_GRADE G
        WHERE YEAR = 2022
        GROUP BY EMP_NO
    ) AS G ON E.EMP_NO = G.EMP_NO
ORDER BY G.SCORE DESC
LIMIT 1
 