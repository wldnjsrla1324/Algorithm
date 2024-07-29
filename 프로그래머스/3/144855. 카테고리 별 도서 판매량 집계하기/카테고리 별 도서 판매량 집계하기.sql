-- 코드를 입력하세요
SELECT B1.CATEGORY, SUM(B2.sales) AS TOTAL_SALES
FROM BOOK AS B1
RIGHT JOIN BOOK_SALES  AS B2
    ON B1.BOOK_ID=B2.BOOK_ID
WHERE B2.SALES_DATE LIKE '2022-01%'
GROUP BY B1.CATEGORY
ORDER BY CATEGORY
