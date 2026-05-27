USE CATALOG supply_chain_demo;

USE SCHEMA gold;

SELECT
  order_status,
  COUNT(*) AS order_count
FROM
  mart_puerto_rico
GROUP BY
  order_status
ORDER BY
  order_count DESC;

SELECT
    MIN(datetime) AS first_date,
    MAX(datetime) AS last_date
FROM mart_puerto_rico;

SELECT
  DATE_TRUNC('month', `datetime`) as month,
  COUNT(DISTINCT `order_id`) as order_count,
  SUM(`total_amount`) as total_revenue
FROM
  `supply_chain_demo`.`gold`.`mart_puerto_rico`
GROUP BY
  DATE_TRUNC('month', `datetime`)
ORDER BY
  month