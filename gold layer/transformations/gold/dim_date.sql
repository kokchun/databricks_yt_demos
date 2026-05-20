CREATE OR REFRESH MATERIALIZED VIEW supply_chain_demo.gold.dim_date
  COMMENT "Dim table - gold layer" AS
SELECT DISTINCT
  CAST(date_format(order_date, 'yyyyMMddHHmm') AS BIGINT) AS datetime_id,
  order_date AS datetime,
  YEAR(order_date) AS year,
  MONTH(order_date) AS month,
  DATE_FORMAT(order_date, 'E') AS weekday,
  HOUR(order_date) AS hour,
  MINUTE(order_date) AS minute
FROM 
  supply_chain_demo.silver.supply_chain_obt;