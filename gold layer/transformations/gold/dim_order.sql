CREATE OR REFRESH MATERIALIZED VIEW supply_chain_demo.gold.dim_order
  COMMENT "Dim table - gold layer" AS
SELECT
  order_id,
  MAX_BY(order_status, order_date) AS order_status
FROM
  supply_chain_demo.silver.supply_chain_obt
GROUP BY
  order_id;