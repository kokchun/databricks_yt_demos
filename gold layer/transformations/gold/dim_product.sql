CREATE OR REFRESH MATERIALIZED VIEW supply_chain_demo.gold.dim_product
  COMMENT "Dim product - gold layer" AS
SELECT
  product_card_id AS product_id,
  MAX_BY(product_name, order_date) AS product_name,
  MAX_BY(category_name, order_date) AS category_name,
  MAX_BY(department_name, order_date) AS department_name,
  MAX_BY(product_price, order_date) AS product_price
FROM
  supply_chain_demo.silver.supply_chain_obt
GROUP BY
  product_card_id;