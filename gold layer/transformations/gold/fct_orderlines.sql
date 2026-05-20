CREATE OR REFRESH STREAMING TABLE supply_chain_demo.gold.fct_orderlines
  COMMENT "Fact table - gold layer" AS
SELECT
  order_item_id,
  order_id,
  customer_id,
  product_card_id AS product_id,
  CAST(date_format(order_date, 'yyyyMMddHHmm') AS BIGINT) AS order_date_id,
  order_item_product_price AS order_price,
  order_item_quantity AS quantity,
  order_item_discount_rate AS discount_rate,
  ROUND(product_price * quantity * (1 - discount_rate), 2) AS total_amount
FROM
  STREAM supply_chain_demo.silver.supply_chain_obt;