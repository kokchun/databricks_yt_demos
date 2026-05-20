CREATE OR REFRESH MATERIALIZED VIEW supply_chain_demo.gold.dim_customer
  COMMENT "Dim table - gold layer" AS
SELECT
  customer_id,
  MAX_BY(customer_fname, order_date) AS first_name,
  MAX_BY(customer_lname, order_date) AS last_name,
  MAX_BY(customer_country, order_date) AS country,
  MAX_BY(customer_state, order_date) AS state,
  MAX_BY(customer_segment, order_date) AS segment
FROM
  supply_chain_demo.silver.supply_chain_obt
GROUP BY
  customer_id;