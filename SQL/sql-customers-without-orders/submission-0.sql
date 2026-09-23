SELECT name
FROM customers
LEFT JOIN orders
    ON customer_id = customers.id
WHERE customer_id is NULL;