#review
SELECT *
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE)
                FROM FOOD_PRODUCT)